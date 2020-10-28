from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask_restful import Api
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import default_exceptions
from flask_sqlalchemy import SQLAlchemy
from application.config import app_config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    CORS(app)

    @app.errorhandler(Exception)
    def handle_error(e):
        code = 500
        if isinstance(e, HTTPException):
            code = e.code
        return jsonify(error=str(e)), code

    for ex in default_exceptions:
        app.register_error_handler(ex, handle_error)

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    api = Api(app)
    api.prefix = '/api'

    from application.controllers.timers import TimersResource
    from application.controllers.exercises import ExercisesResource

    api.add_resource(TimersResource, '/timers', '/timers/<int:timer_id>')
    api.add_resource(ExercisesResource, '/exercises', '/exercises/<int:exercise_id>')

    return app
