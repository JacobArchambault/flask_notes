import os
from flask import Flask, redirect, url_for
from flask_migrate import Migrate 
from dotenv import load_dotenv, find_dotenv
from notes.notes import note_blueprint
from notes.error.error import page_not_found
from notes.registration.registration import registration_blueprint
from .models import db

load_dotenv(find_dotenv())

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', default='dev')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)    

    db.init_app(app)
    migrate = Migrate(app, db)

    @app.route('/')
    def index():
        return redirect(url_for('notes.note_index'))

    app.register_blueprint(note_blueprint)
    app.register_error_handler(404, page_not_found)
    app.register_blueprint(registration_blueprint)
    return app