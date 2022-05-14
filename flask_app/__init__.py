from flask import Flask
from dotenv import load_dotenv
import os
from . import sentiment

def create_app():
    load_dotenv()

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.getenv('SECRET_KEY', 'dev'),
    )

    app.register_blueprint(sentiment.bp)

    return app