# VetApi

## Estructura del Proyecto:

````
VetApi/
├── src/
│   ├── database/ --> Conexión con la BD
│   │   ├── __init__.py
│   │   └── db.py
│   ├── models/ --> Definición de Clases (representa Entidades de la BD)
│   │   ├── __init__.py
│   │   ├── appointment_model.py
│   │   ├── customer_model.py
│   │   ├── pet_model.py
│   │   ├── session_model.py
│   │   └── user_model.py
│   ├── routes/ --> Definición de Endpoints
│   │   ├── __init__.py
│   │   ├── appointment_routes.py
│   │   ├── auth_routes.py
│   │   ├── customer_routes.py
│   │   ├── pet_routes.py
│   │   └── user_routes.py
│   ├── service/ --> Lógica de negocio
│   │   ├── __init__.py
│   │   └── ...
│   └── tests/ --> Archivos de test varios
│       ├── create_user.py --> Testeo creación de usuarios
│       └── db_connection_test.py --> Testeo la conexión con la BD
├── BdVeterinaria.sql --> Archivo para la creación de la BD.
├── requirements.txt --> Paquetes necesarios para correr la app.
├── config.py --> Archivo con la configuración esencial de la App (flask, SqlAlchemy, ...)
└── app.py --> Aplicación principal.

````

## Configuración Inicial y Ejecución de la Aplicación Flask:

(Asegúrate de estar en el directorio raíz del proyecto: `VetApi/`)

### 1. Entorno Virtual:
1.  **Crear entorno virtual:**
    ```bash
    python3 -m venv .venv
    ```
2.  **Activar entorno virtual:**
    *   **macOS/Linux:**
        ```bash
        source .venv/bin/activate
        ```
    *   **Windows (Git Bash o similar):**
        ```bash
        source .venv/Scripts/activate
        ```
    *   **Windows (Command Prompt o PowerShell):**
        ```bash
        .\.venv\Scripts\activate
        ```

### 2. Instalar Dependencias:
Una vez activado el entorno virtual, instala los paquetes necesarios:
```bash
pip install -r requirements.txt
```

### 3. Crear la BD en Mysql:
Se necesita tener una BD llamada "veterinary_db", este se puede crear en local. Se adjunta el 
archivo "BdVeterinaria.sql" para ejecutarlo en Mysql y preparar la BD.

### 4. Crear archivo de .env
Crear un archivo .env en la raiz del proyecto (VetApi/), y añadir le siguiente contenido, adaptandolo:
```
# Aqui meter las variables de entorno

# Configuración de la Base de Datos MySQL
DB_USER="usuario BD"
DB_PASSWORD="contraseña usuario BD"
DB_HOST="localhost" # o la IP de tu servidor MySQL
DB_PORT="3306"      # Puerto por defecto de MySQL
DB_NAME="veterinary_db" # El nombre de tu base de datos (asegúrate de que exista)

# SQLAlchemy Database URI
SQLALCHEMY_DATABASE_URI="mysql+pymysql://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS=False

# JWT
JWT_KEY="Key segura de JWT"
```