from app import db

class Chocolate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)
    wines = db.relationship("Wine", backref="chocolate", lazy=True)

    def to_dict(self):
        return {
            "id": self.id, 
            "name": self.name, 
            "wines": [wine.to_dict() for wine in self.wines]
        }

class Wine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)
    chocolate_id = db.Column(db.Integer, db.ForeignKey("chocolate.id"), nullable=True)

    def to_dict(self):
        return {"id": self.id, "name": self.name}