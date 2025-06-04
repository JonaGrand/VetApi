from src.database.db import db
from werkzeug.security import generate_password_hash, check_password_hash

#class RolEnum(enum.Enum):
#    VETERINARIO = 'veterinario'
#    ASMINISTRADOR = 'administrador'
#    SECRETARIO = 'secretario'

class User(db.Model):
    __tablename__ = 'Users'

    dni = db.Column(db.String(9), primary_key=True, nullable=False)
    name = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    surnames = db.Column(db.String(200), nullable=False)
    rol = db.Column(db.String(200), nullable=False) # vet, admin, gest
    mail = db.Column(db.String(200), nullable=False, unique=True)  # Asumo que el correo debe ser único
    phone = db.Column(db.String(200), nullable=False)
    admission_date = db.Column(db.Date, nullable=False)

    # Hashear contraseña
    def set_password(self, password_to_set):
        self.password = generate_password_hash(password_to_set)

    # Comprobar hash contraseña (validar contraseña)
    def check_password(self, password_to_check):
        return check_password_hash(self.password, password_to_check)

    def __repr__(self):
        return f'<User {self.dni} - {self.name} {self.surnames}>'

    def to_dict(self):
        return {
            'dni': self.dni,
            'name': self.name,
            'surnames': self.surnames,
            'rol': self.rol,
            'mail': self.mail,
            'phone': self.phone,
        }
