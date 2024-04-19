from flask_restful import Resource, request, reqparse
from db.tiger_bets.users import clear_users,get_user,delete_user,delete_user_admin,create_user,create_user_admin,update_user,update_user_admin,update_user_session_id,validate_user,invalidate_user,User,get_users_by_query
from constants import BAD_REQUEST_ERROR, HELP

class Users(Resource):
    """
    implement user actions
    """
    def get(self):
        """
        handle get requests
        """
        pass

    def post(self, action):
        """
        handle user post requests
        """
        if action == 'register':
            return self.register()
        elif action == 'login':
            return self.login()
        elif action == 'logoff':
            return self.logoff()
        elif action == 'clear':
            clear_users()
        elif action == 'find_user':  # I know this is bad practice, but it's 3 AM
            return self.find_user()    
        else:
            return BAD_REQUEST_ERROR, 400

    def login(self):
        """
        user login function
        """
        parser = reqparse.RequestParser()
        parser.add_argument('username', help=HELP, required=True)
        parser.add_argument('password', help=HELP, required=True)

        data = parser.parse_args()

        if not validate_user(data['username'], data['password']):
            return {"error": "username or password is incorrect"}, 401

        session_id = update_user_session_id(data['username'])
        user = get_user(data['username'], session_id)
        return {"user": user.to_json(), "session_id": session_id}, 200

    def register(self):
        """
        register user action
        """
        parser = reqparse.RequestParser()
        parser.add_argument('username', help=HELP, required=True)
        parser.add_argument('fullname', help=HELP, required=True)
        parser.add_argument('email', help=HELP, required=True)
        parser.add_argument('password', help=HELP, required=True)
        data = parser.parse_args()

        try:
            password = data["password"]
            user = User("uid", data["username"], data["fullname"], data["email"])

            if create_user(user, password):
                return {"user": user.to_json()}, 200
            else:
                return {"error": "username is not unique"}, 401
        except ValueError:
            return {"error": "Invalid parameters"}, 400

    def logoff(self):
        """
        user logoff function
        """
        parser = reqparse.RequestParser()
        parser.add_argument('session', help=HELP, required=True)
        data = parser.parse_args()

        if not invalidate_user(data['session']):
            return {"error": "user could not be logged off"}, 401
        return {"success": "logoff successful"}, 200

    def find_user(self):
        """
        handle post requests
        """
        parser = reqparse.RequestParser()
        parser.add_argument('username', help=HELP, required=True)
        parser.add_argument('session', help=HELP, required=True)
        data = parser.parse_args()

        user = get_user(data['username'], data['session'])
        if user is None:
            return {"error": "user could not be found"}, 401
        return {"user": user.to_json()}, 200
    
    def put(self, action):
        """
        handle user post requests
        """
        if action == 'update':
            return self.update()
        elif action == 'deactivate':
            return self.deactivate()  
        else:
            return BAD_REQUEST_ERROR, 400

    def update(self):
        """
        put request to change account information
        """
        parser = reqparse.RequestParser()
        parser.add_argument('newuser', help=HELP, required=True)
        parser.add_argument('newname', help=HELP, required=True)
        parser.add_argument('newemail', help=HELP, required=True)
        parser.add_argument('session', help=HELP, required=True)
        data = parser.parse_args()

        if not update_user(data['newuser'], data['newname'], data['newemail'], data['session']):
            return {"error": "failed to update user"}, 401
        target = get_user(data['newuser'], data['session'])
        return {"user": target.to_json()}, 200
    
    def deactivate(self):
        """
        put request to deactivate account
        """
        parser = reqparse.RequestParser()
        parser.add_argument('username', help=HELP, required=True)
        parser.add_argument('session', help=HELP, required=True)
        data = parser.parse_args()

        if not delete_user(data['session']):
            return {"error": "failed to delete user"}, 401
        deleted = get_user(data['username'], data['session'])
        return {"user": deleted.to_json()}, 200

class Admin(Resource):
    def get(self):
        """
        handle get requests
        """
        return
    
    def post(self, action):
        """
        handle user post requests
        """
        if action == 'find_users':  # I know this is bad practice, but it's 3 AM
            return self.find_users()
        elif action == 'register':
            return self.reg_admin()    
        else:
            return BAD_REQUEST_ERROR, 400
    
    def find_users(self):
        """
        find users function
        """
        parser = reqparse.RequestParser()
        parser.add_argument('username', help=HELP, required=True)
        parser.add_argument('session', help=HELP, required=True)

        data = parser.parse_args()
        user_list = get_users_by_query(data['username'], data['session'])
        if user_list is None:
            return {"error": "Invalid Request: user is not admin"}, 401
        return {"users": user_list}, 200
    
    def reg_admin(self):
        """
        register admin account (TEST ONLY. MY INITIAL PLAN WAS TO INTERNALLY CREATE THESE ACCOUNTS IN ADVANCE)
        """
        parser = reqparse.RequestParser()
        parser.add_argument('username', help=HELP, required=True)
        parser.add_argument('fullname', help=HELP, required=True)
        parser.add_argument('email', help=HELP, required=True)
        parser.add_argument('password', help=HELP, required=True)
        data = parser.parse_args()

        try:
            password = data["password"]
            user = User("uid", data["username"], data["fullname"], data["email"])

            if create_user_admin(user, password):
                return {"user": user.to_json()}, 200
            else:
                return {"error": "username is not unique"}, 401
        except ValueError:
            return {"error": "Invalid parameters"}, 400

    def put(self, action):
        """
        handle user post requests
        """
        if action == 'update':
            return self.update()
        elif action == 'deactivate':
            return self.deactivate()  
        else:
            return BAD_REQUEST_ERROR, 400

    def update(self):
        """
        put request to change specified account information
        """
        parser = reqparse.RequestParser()
        parser.add_argument('username', help=HELP, required=True)
        parser.add_argument('newuser', help=HELP, required=True)
        parser.add_argument('newname', help=HELP, required=True)
        parser.add_argument('newemail', help=HELP, required=True)
        parser.add_argument('session', help=HELP, required=True)
        data = parser.parse_args()

        if not update_user_admin(data['username'], data['newuser'], data['newname'], data['newemail'], data['session']):
            return {"error": "Invalid Request: user is not admin or target username not found"}, 401
        target = get_user(data['newuser'], data['session'])
        return {"user": target.to_json()}, 200
    
    def deactivate(self):
        """
        put request to deactivate specified account
        """
        parser = reqparse.RequestParser()
        parser.add_argument('username', help=HELP, required=True)
        parser.add_argument('session', help=HELP, required=True)
        data = parser.parse_args()

        if not delete_user_admin(data['username'], data['session']):
            return {"error": "Invalid Request: user is not admin or failed to delete target username"}, 401
        deleted = get_user(data['username'], data['session'])
        return {"user": deleted.to_json()}, 200