from flask import request
from flask_restful import Resource
from flask.json import jsonify
from db.tiger_bets.events import *

class Events(Resource):
    # Lists events with results and team names
    def get(self):
        assign_random_event_results()
        return list_events_with_team_names()

    # Creates a new event from form data
    def post(self):
        event_name = request.form.get("event_name")
        team_a_id = request.form.get("team_a_id")
        team_b_id = request.form.get("team_b_id")
        return create_event(event_name, team_a_id, team_b_id)

class SingleEvent(Resource):
    # Returns details for a specific event ID
    def get(self, event_id):
        event = get_event_details(event_id)
        if event:
            return jsonify(event)
        else:
            return jsonify({'message': 'Event not found'}), 404

    # Updates an event based on form data and event ID
    def put(self, event_id):
        data = request.form
        result = edit_event(event_id, data)
        if result == "Success":
            return {0: "Success"}, 200
        return result, 500

    # Removes an event by ID
    def delete(self, event_id):
        return delete_event(event_id)
