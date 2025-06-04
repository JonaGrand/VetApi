from src.database.db import db
from datetime import datetime # timedelta se usará donde se crea la sesión

class Session(db.Model):
    __tablename__ = 'Sessions'

    id = db.Column(db.String(200), primary_key=True)  # JTI del token
    user_id = db.Column(db.String(9), db.ForeignKey('Users.dni', ondelete='CASCADE'), nullable=False) # Asegúrate que 'Users.dni' sea correcto
    expires_at = db.Column(db.DateTime, nullable=False) # Campo para la fecha de expiración

    # Relación para acceder al usuario desde la sesión y viceversa
    # user = db.relationship('User', backref=db.backref('sessions', lazy=True))

    def __repr__(self):
        return f'<Session {self.id} for user {self.user_id} expiring at {self.expires_at}>'