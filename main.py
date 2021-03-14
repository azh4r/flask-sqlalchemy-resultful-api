from data import initialize
from resources import add_resource
from flask import Flask
from flask_restful import Api


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
initialize(app)
api = Api(app)
add_resource(api)

if __name__ == "__main__":
    app.run(debug=True)