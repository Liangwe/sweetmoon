from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from api import api_blue
from config import Config
from models import *


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_blue)
    app.config.from_object(Config())
    db.init_app(app)
    Migrate(app, db)
    CORS(app, supports_credentials=True)
    return app


app = create_app()


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    print(app.route)
    app.run(host="0.0.0.0", port=8000)
