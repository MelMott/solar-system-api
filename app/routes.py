from flask import Blueprint,jsonify, abort, make_response


class Planet:
    def __init__(self, id, name, description, age):
        self.id = id
        self.name = name
        self.description =  description
        self.age = age

planets = [
    Planet(1, 'Mercury', 'First and smaller planet in the solar system.', 4.5), Planet(2,'Venus', 'Second planet in the solar system. Hottest planet in the solar system', 4.6),
    Planet(3, 'Earth', 'Seventy percent of its surface is compose of water. Third planet in the solar system', 4.5), Planet(4, 'Mars', 'Fourth planet in the solar system. Mars its called the red planet', 4.6),
    Planet(5, 'Jupiter', 'Swriling clouds and the fisth planet on the solar system', 4.6), Planet(6, 'Saturn', 'Sixth planet in the solar system and it has rings.', 4.5),
    Planet(7, 'Uranus', 'An ice giant. Seventh planet in the solar system', '4.5'), Planet(8, 'Neptune', 'Dark and cold planet. Eight planet in the solar system', 4.5)]


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("/<planets_id>", methods=["GET"])
def handle_one_planet(planet_id):
    planet_id = int(planet_id)
    for planet in planets:
        if planet.id == planet_id:
            return({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "age": planet.age
            })

@planets_bp.route("", methods=["GET"])
def handle_planets():
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "age": planet.age
        })
        
    return jsonify(planets_response), 200

def validate_planet(planet_id):
    try:
        planet.id = int(planet_id)
    except:
        abort(make_response({"message":f"Id planet {planet_id} invalid."}, 400))
    for planet in planets:
        if planet_id == planet_id:
            return planet
    abort(make_response({"message":f"Planet {planet.name} not found."}, 404))
        
    
        