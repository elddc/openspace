from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.post("/foo")
def foo():
    # post requests can access data with request.json[key]
    return str(request.json["busyness"])

@app.get("/bar")
def bar():
    # get requests can access data with request.args.get(key)
    return str(request.args.get("building"))
