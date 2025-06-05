from src.database.db import db


class Customer(db.Model):
    __tablename__ = 'Customers'

    dni = db.Column(db.String(9), primary_key=True, nullable=False)
    name = db.Column(db.String(200), nullable=False)
    surnames = db.Column(db.String(200), nullable=False)
    mail = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(9), nullable=False)
    
    def to_dict(self):
        return {
            'dni': self.dni,
            'name': self.name,
            'surnames': self.surnames,
            'mail': self.mail,
            'phone': self.phone,
        }