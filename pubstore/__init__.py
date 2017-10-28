from .library import init_db
from .res import Keys
from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

api.add_resource(Keys, '/keys')

