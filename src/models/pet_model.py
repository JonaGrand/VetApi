from src.database.db import db

class Pet(db.Model):
    __tablename__ = 'Pets'
    num_chip = db.Column(db.Integer, primary_key=True ,nullable=False)
    name = db.Column(db.String(200), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    animal = db.Column(db.String(200), nullable=False)
    breed = db.Column(db.String(200), nullable=False)
    customer_id = db.Column(db.String(9), nullable=False)

    def to_dict(self):
        return {
            'num_chip': self.num_chip,
            'name': self.name,
            'birth_date': self.birth_date,
            'animal': self.animal,
            'breed': self.breed,
            'customer_id': self.customer_id,
        }