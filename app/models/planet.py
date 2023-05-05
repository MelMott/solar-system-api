from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    
    def to_dict(self):
        return{
            "id": self.id,
            "name": self.id,
            "description": self.description
        }
    
    @classmethod
    def from_dict(cls, planet_details):
        new_planet = cls(
            name=planet_details["name"],
            description=planet_details["description"]
        )
        return new_planet
