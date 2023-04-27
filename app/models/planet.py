from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    surface_area = db.Column(db.String)
    moons = db.Column(db.Integer)
    distance_from_sun = db.Column(db.BigInteger)
    namesake = db.Column(db.String)