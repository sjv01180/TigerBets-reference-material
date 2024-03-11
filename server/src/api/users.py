from flask_restful import Resource, request
from flask.json import jsonify
from db.tiger_bets.users import *


class Users(Resource):
    def get(self):
        return