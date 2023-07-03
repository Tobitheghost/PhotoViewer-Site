from flask import Flask
from os import path
def create_app():
    app = Flask(__name__)

    from .photoviewr import photoviewer
    app.register_blueprint(photoviewer, url_prefix='/')
    return app

