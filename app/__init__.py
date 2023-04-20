from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    from .routes import planets_pb
    app.register_blueprint(planets_pb)
    return app
