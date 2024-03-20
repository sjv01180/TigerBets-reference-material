from flask_restful import Resource, reqparse, request

from db.db_utils import *
from db.tiger_bets.bets import rebuild_bet_tables


class Init(Resource):
    def post(self):
        rebuild_bet_tables()
        return {0: "Success"}, 200


class Version(Resource):
    def get(self):
        return exec_get_one("SELECT VERSION()")