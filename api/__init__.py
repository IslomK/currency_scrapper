from flask import Flask
from config import DEBUG

app = Flask(__name__, instance_relative_config=False)


def create_app():
    """Construct the core application."""
    if DEBUG:
        app.config.from_object('config.DevelopmentConfig')
    else:
        app.config.from_object('config.ProductionConfig')

    with app.app_context():
        from . import routes

        return app