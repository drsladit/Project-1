from flask import Flask,jsonify
from flask_restful import Api, Resource
import json

app = Flask(__name__)
api = Api(app)

with open("Top 30days Installs in JSON", mode='r') as data_30days:
    Top_30days_Installs = json.load(data_30days)


@app.route('/')
def index():
    return "Welcome to the API"

@app.route('/Topapps', methods=['GET'])
def get():
    return Top_30days_Installs




if __name__ == "__main__":
    app.run(debug=True)