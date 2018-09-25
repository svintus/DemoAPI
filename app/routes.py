from app import app
from flask import request, jsonify

@app.route('/', methods=['GET'])
def get():
    return "Hello, World!"

@app.route('/', methods=['POST'])
def post():
    json = request.get_json()
    print(json)
    return ""
