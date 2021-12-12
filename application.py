# Test application for pythonanywhere

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello Testing"

# @app.route('iceData/<int:id>')
# def getID(id):
# 	return str(id)

if __name__ == '__main__':
	app.run(debug = True)