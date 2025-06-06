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
│   └── services/ --> Lógica de negocio
│       └── ...
├── BdVeterinaria.sql --> Archivo para la creación de la BD.
├── requirements.txt --> Paquetes necesarios para correr la app.
├── config.py --> Archivo con la configuración esencial de la App (flask, SqlAlchemy, ...)
├── crate_user_test.py --> Archivo con usuario de test
└── app.py --> Aplicación principal.