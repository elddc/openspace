from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.post("/foo")
def foo():
    return request.json["building"]

@app.get("/bar")
def bar():
    return request.args.get("building")
