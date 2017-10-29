from .library import init_db
from .res import Keys
from flask import Flask, request
from flask_restful import Api
from pprint import pprint

app = Flask(__name__)
api = Api(app)

api.add_resource(Keys, '/keys')


@app.before_request
def log_request():
    return None
