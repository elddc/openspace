from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.post("/foo")
def foo():
    print(request.data)
    return "yay"

@app.get("/bar")
def bar():
    return "hello world"
