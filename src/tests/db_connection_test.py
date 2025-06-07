import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener la URI de la base de datos desde las variables de entorno
db_uri = os.getenv('SQLALCHEMY_DATABASE_URI')

if not db_uri:
    print("Error: La variable de entorno SQLALCHEMY_DATABASE_URI no está configurada.")
    print("Asegúrate de que tu archivo .env está presente y configurado correctamente.")
else:
    print(f"Intentando conectar a: {db_uri.replace(os.getenv('DB_PASSWORD', '******'), '******')}") # Ocultar contraseña en la salida
    try:
        # Crear un motor de SQLAlchemy
        engine = create_engine(db_uri)

        # Intentar establecer una conexión
        with engine.connect() as connection:
            # Ejecutar una consulta simple para verificar la conexión
            result = connection.execute(text("SELECT 1"))
            for row in result:
                print("Resultado de la consulta SELECT 1:", row[0])
            print("¡Conexión a la base de datos exitosa!")

    except SQLAlchemyError as e:
        print(f"Error al conectar a la base de datos: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")