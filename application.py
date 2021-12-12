# Test application for pythonanywhere

from flask import flask

app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/')
def index():
	return "Hello"

@app.route('iceData/<int:id>')
def getID(id):
	return str(id)

if __name__ == '__main__' :
	app.run(debug = True)