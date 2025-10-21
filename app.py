
from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/api/backlog')
def get_backlog():
    with open('static/backlog.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/')
def home():
    return "Offshore Wind Intelligence API is running."
