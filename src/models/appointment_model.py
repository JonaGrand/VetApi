from src.database.db import db


class Appointment(db.Model):
    __tablename__ = 'Appointments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.String(9), db.ForeignKey('Users.dni'), nullable=False)
    pet_id = db.Column(db.String(10), db.ForeignKey('Pets.num_chip'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'description': self.description,
            'date': self.date,
            'user_id': self.user_id,
            'pet_id': self.pet_id
        }