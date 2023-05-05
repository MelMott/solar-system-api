from app import db
from app.models.planet import Planet
from flask import Blueprint,jsonify, abort, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

def validate_planet(id):
    model = Planet
    try:
        id = int(id)
    except:
        abort(make_response({"message":f"Id planet {id} invalid."}, 400))

    planet = model.query.get(id)

    if not planet:
        return abort(make_response({"message":f"{model.__name__} with id {id} not found."}, 404))
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
    
    planet_query = request.args.get("name")
    if planet_query:
        planets = Planet.query.filter_by(name=planet_query)
    else:
        # How do I get all of the books from the DB? SQLAlchemy does it with .query.all()
        planets = Planet.query.all()
    
    planets_response = []
    
    for planet in planets:
        planets_response.append(planet.to_dict())
        # Below is what we have previously, I changed it to_dict per lesson)
        # planets_response.append(
        #     {
        #         "id": planet.id,
        #         "name": planet.name,
        #         "description": planet.description
        #     }
        # )
    return jsonify(planets_response), 200

#changes here from class 5/5
def make_planet(planet_details):
    new_planet = Planet(
        name=planet_details["name"],
        description=planet_details["description"]
    )
    return new_planet

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet_by_id(planet_id):

    # Call validate to check if book exists-It returns a book if it exists
    planet = validate_planet(planet_id)
    
    return planet.to_dict(), 200

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_one_planet(planet_id):
    planet_to_delete = validate_planet(Planet, planet_id)

    db.session.delete(planet_to_delete)
    db.session.commit()

    return f"Planet #{planet_to_delete.id} successfully deleted", 200

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):

    planet_to_update = validate_planet(Planet, planet_id)
    request_body = request.get_json()

    if "name" not in request_body or "description" not in request_body:
        return make_response("Invalid Request", 400)

    planet_to_update.name = request_body["name"]
    planet_to_update.description = request_body["description"]

    db.session.commit()

    return planet_to_update.to_dict(), 200
    # Commented out the below, because I saw this refactoring in class today. 
    #return make_response(f"Planet #{planet.id} suscessfully updated")

        
    
        