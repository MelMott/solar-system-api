from app import db
from app.models.planet import Planet
from flask import Blueprint,jsonify, abort, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"message":f"Id planet {planet_id} invalid."}, 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        return abort(make_response({"message":f"Planet {planet_id} not found."}, 404))
    return planet

@planets_bp.route("", methods=["POST"])
def create_planet():
    
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"], description=request_body["description"])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name}, succesfully created", 201)
    
@planets_bp.route("", methods=["GET"])
def read_all_planets():
    
    planets = Planet.query.all()
    planets_response = []
    
    for planet in planets:
        planets_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description
            }
        )
    return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_book_by_id(book_id):

    # Call validate to check if book exists-It returns a book if it exists
    planet = validate_planet(book_id)
    
    return {"id": planet.id,
            "name": planet.title,
            "description": planet.description}


        
    
        