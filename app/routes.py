from app import db
from app.models.planet import Planet
from flask import Blueprint,jsonify, abort, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("/<planet_id>", methods=["POST"])
def create_planet(planet_id):
    
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"], surface_area=request_body["surface_area"], moons=request_body["moons"], distance_from_sun=request_body["distance_from_sun"], namesake=request_body["namesake"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name}, succesfully created", 201)
    # planet = validate_planet(planet_id)
    # planet_id = int(planet_id)
    # for planet in planets:
    #     if planet.id == planet_id:
    #         return({
    #             "id": planet.id,
    #             "name": planet.name,
    #             "description": planet.description,
    #             "age": planet.age
            # })

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
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"Id planet {planet_id} invalid."}, 400))
    for planet in planets:
        if planet.id == planet_id:
            return planet
    abort(make_response({"message":f"Planet {planet_id} not found."}, 404))
        
    
        