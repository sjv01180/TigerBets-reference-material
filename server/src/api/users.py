from flask_restful import Resource, request, reqparse
from db.tiger_bets.users import *


class Users(Resource):
    """
    implement user actions
    """
    def get(self):
        return

    def post(self, action):
        """
        handle user post requests
        """
        if action == 'register':
            return self.register()
        elif action == 'login':
            return self.login()
        elif action == 'clear':
            clear_users()
        else:
            return {"error": "Bad Request"}, 400

    def login(self):
        """
        user login function
        """
        parser = reqparse.RequestParser()
        parser.add_argument('username', help='This field cannot be blank', required=True)

        data = parser.parse_args()

        user = get_user_by_username(data["username"])
        if user is None:
            return {"error": "username is incorrect"}, 401

        session_id = update_user_session_id(user)
        return {"user": user.to_json(), "session_id": session_id}, 200

    def register(self):
        """
        register user action
        """
        parser = reqparse.RequestParser()
        parser.add_argument('username', help='This field cannot be blank', required=True)
        parser.add_argument('fullname', help='This field cannot be blank', required=True)
        parser.add_argument('email', help='This field cannot be blank', required=True)
        data = parser.parse_args()

        try:
            user = User(data["username"], data["fullname"], data["email"])

            if create_user(user):
                return {"user": user.to_json()}, 200
            else:
                return {"error": "username exists"}, 401
        except ValueError:
            return {"error": "Invalid parameters"}, 400
