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

# 1. Ejecutar app Flask:

(Tienes que estar en la raiz del proyecto: VetApi/)

**Aplicación principal:** python3 app.py
**Tests:**
- create_user_test.py:  python3 -m src.tests.create_user_test
- db_test.py: python3 src.test.db_connection_test
