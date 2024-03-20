from flask import request
from flask_restful import Resource
from flask.json import jsonify

from db.tiger_bets.bets import *
import json


class Bets(Resource):
    def get(self):
        return list_user_bets()

    def post(self):
        user_id = request.form.get("user_id")
        event_id = request.form.get("event_id")
        team_id = request.form.get("team_id")
        points = request.form.get("points")
        
        return create_bet(
            user_id, event_id, team_id, points
        )


class Bet(Resource):
    def get(self, bet_id):
        return jsonify(get_bet_details(bet_id))

    def put(self, bet_id):
        data = request.form
        result = edit_bet(bet_id, data)
        if result == "Success":
            return {0: "Success"}, 200
        return result, 500

    def delete(self, bet_id):
        return delete_bet(bet_id)
