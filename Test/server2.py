from flask import Flask, url_for, request, redirect, abort, jsonify
from flask_cors import CORS
from carbonDao2 import carbonDao2

app = Flask(__name__, static_url_path='', static_folder='staticpages')
CORS(app)


@app.route('/')
def index():
    return "Test2"


# get all
@app.route('/iceData2')
def getAll():
    return jsonify(carbonDao2.getAll())


# find By id
@app.route('/iceData2/<int:ID>')
def findByID(ID):
    return jsonify(carbonDao2.findByID(ID))

# create
# curl -X POST -d "{\"Material\":\"test\", \"Density\":123}" http://127.0.0.1:5000/iceData


@app.route('/iceData2', methods=['POST'])
def create():
   
    if not request.json:
        abort(400)

    elem = {
        "ID": request.json["ID"],
        "Material": request.json["Material"],
        "Density": request.json["Density"],
        "EmbodiedCarbon": request.json["EmbodiedCarbon"]
    }
    return jsonify(carbonDao2.create(elem))

#update
# curl -X PUT -d "{\"Material\":\"new Title\", \"Density\":999}" -H "content-type:application/json" http://127.0.0.1:5000/iceData/1


@app.route('/iceData2/<int:ID>', methods=['PUT'])
def update(ID):
    foundElem=carbonDao2.findById(ID)
    print (foundElem)
    if foundElem == {}:
        return jsonify({}), 404
    currentElem = foundElem
    if 'Material' in request.json:
        currentElem['Material'] = request.json['Material']
    if 'Density' in request.json:
        currentElem['Density'] = request.json['Density']
    if 'EmbodiedCarbon' in request.json:
        currentElem['EmbodiedCarbon'] = request.json['EmbodiedCarbon']
    carbonDao2.update(currentElem)

    return jsonify(currentElem)

#delete
# curl -X DELETE http://127.0.0.1:5000/iceData/1


@app.route('/iceData2/<int:ID>', methods=['DELETE'])
def delete(ID):
    carbonDao2.delete(ID)

    return jsonify({"done": True})


if __name__ == "__main__":
    app.run(debug=True)
