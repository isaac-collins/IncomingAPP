import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"]=True

sample_data = [
    {
        "id": 1,
        "data": "data1"
    },
    {
        "id": 2,
        "data": "data2"
    }

]

@app.route('/')
def api_test():
    return "foo"

@app.route('/sample', methods=["GET"])
def api_sample():
    if id in request.args:
        id = int(request.args["id"])
    else:
        print("error")
    resp = []
    for data in sample_data:
        if data['id'] == id:
            resp.append(data)
    return jsonify(resp)
