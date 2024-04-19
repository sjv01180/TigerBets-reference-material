from flask_restful import Resource, reqparse, request

from db.db_utils import exec_get_one
from db.tiger_bets.events import rebuild_event_tables
from db.tiger_bets.bets import rebuild_bet_tables

class Init(Resource):
    def post(self):
        rebuild_event_tables()
        rebuild_bet_tables()
        return {0: "Success"}, 200

class Version(Resource):
    def get(self):
        return exec_get_one("SELECT VERSION()")