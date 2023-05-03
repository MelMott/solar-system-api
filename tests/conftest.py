import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def three_saved_planets(app):
    planet_one = Planet(id=1, name="Jupiter", description="King of the Roman gods, aka Zeus")
    planet_two = Planet(id=2, name="Mars", description="Roman god of war, aka Ares")
    planet_three = Planet(id=3, name="Venus", description="Roman goddess of love, aka Aphrodite")

    db.session.add(planet_one)
    db.session.add(planet_two)
    db.session.add(planet_three)

    db.session.commit()
