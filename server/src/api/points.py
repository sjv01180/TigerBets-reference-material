from flask import request
from flask_restful import Resource
from flask.json import jsonify

from db.tiger_bets.points import *

class Point(Resource):
    def put(self):
        user_id = request.form.get("user_id")
        points = request.form.get("points", type=int)
        response = update_points(user_id, points)
        return jsonify(response)

    def get(self, user_id):
        response = get_points_for_user(user_id)
        return jsonify(response)

class Points(Resource):
    def get(self):
        top_users = get_users_with_top_points()
        return jsonify(top_users)