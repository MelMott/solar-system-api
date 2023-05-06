from app import db
from app.models.planet import Planet
from flask import Blueprint,jsonify, abort, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

# Added model as param to validate_planet. Model receives the Planet class.
def validate_planet(model, id):
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

    # Added this piece for input validation to Post
    if not "name" in request_body or not "description" in request_body:
        return make_response({"details": "Invalid data"}, 400)

    new_planet = Planet.from_dict(request_body)

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

    return jsonify(planets_response), 200

# Deleted the method that was building a planet dict because I was not in use
# That method is pretty much the same as the one in class planet

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet_by_id(planet_id):

    # Call validate to check if book exists-It returns a book if it exists
    planet = validate_planet(Planet, planet_id)
    
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

    # Deleted validation here because it put can modify only a fraction of a record
    # The validation was not neccesary

    planet_to_update.name = request_body["name"]
    planet_to_update.description = request_body["description"]

    db.session.commit()

    return planet_to_update.to_dict(), 200

        
    
        