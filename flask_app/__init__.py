from http.client import HTTPException
from flask import (Flask, jsonify)
from dotenv import load_dotenv
import os
from .endpoints import sentiment
from werkzeug.exceptions import default_exceptions
from tweepy import HTTPException as tweepy_HTTPException


def create_app():
    load_dotenv()

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.getenv('SECRET_KEY', 'dev'),
    )

    app.register_blueprint(sentiment.bp)

    @app.errorhandler(Exception)
    def handle_exception(err):
        error_code = 500
        message = 'There was an error with our API :('

        if isinstance(err, HTTPException):
            error_code = err.code
        elif isinstance(err, tweepy_HTTPException):
            if len(err.api_codes) != 0:
                error_code = err.api_codes[0]
            if len(err.api_messages) != 0:
                message = err.api_messages[0]

        return jsonify(error=str(err), message=message), error_code

    for exceptions in default_exceptions:
        app.register_error_handler(exceptions, handle_exception)

    return app
