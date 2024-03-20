from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from api.management import *
from api.users import *
from api.bets import *

app = Flask(__name__)
CORS(app)
api = Api(app)

# Management APIs
api.add_resource(Init, "/manage/init")
api.add_resource(Version, "/manage/version")

# User APIs
api.add_resource(Users, "/users")

# Bet APIs
api.add_resource(Bets, "/bets")
api.add_resource(Bet, "/bets/<string:bet_id>")

if __name__ == "__main__":
    app.run(debug=True, port=8080)