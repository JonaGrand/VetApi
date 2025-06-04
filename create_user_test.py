from app import create_app, db  # Importa tu app y db
from src.models.user_model import User
from datetime import date
# Si estás hasheando contraseñas, importa tu función de hash aquí

# Crea la aplicación para establecer el contexto
app = create_app()

# Empuja un contexto de aplicación
with app.app_context():
    try:
        # Crea un nuevo empleado
        new_User = User(
            dni='12345678T',
            name='test',
            surnames='test',
            rol='vet', # Usa el miembro del Enum directamente
            mail='testsqlalchemy@example.com',
            phone='123456789',
            admission_date=date(2024, 1, 15)
        )
        # Usamos esta función para poner la contraseña.
        new_User.set_password('test-password')

        # Añade el nuevo empleado a la sesión
        db.session.add(new_User)

        # Guarda los cambios en la base de datos
        db.session.commit()
        print(f"Usuario '{new_User.name}' creado con éxito.")

    except Exception as e:
        db.session.rollback()  # Revierte los cambios en caso de error
        print(f"Error al crear el Usuario: {e}")
    finally:
        db.session.close()
        db.session.close()