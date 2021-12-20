# Test application for pythonanywhere

from flask import Flask, url_for, request, redirect, abort, jsonify
from flask_cors import CORS

app = Flask(__name__, static_url_path='', static_folder='staticpages')
CORS(app)

@app.route('/')
def index():
	return "Hello Testing"

if __name__ == '__main__':
	app.run(debug = True)