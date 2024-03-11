from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from api.users import *

app = Flask(__name__)
CORS(app)
api = Api(app)

# User APIs
api.add_resource(Users, "/users")

if __name__ == "__main__":
    app.run(debug=True, port=8080)