from flask import Flask, request
from flask_cors import CORS
from sqlalchemy.orm import Session

app = Flask(__name__)
CORS(app)

@app.post("/foo")
def foo():
    # post requests can access data with request.json[key]
    # __tablename__
    # id
    # name
    # address
    # location
    # capacity
    # busyness
    # rooms
    # inputs
    # last_updated

    # building_id
    # room_number
    # busyness


    # with Session(engine) as session:
    user = model.Building(
        # id="",
        name=str(request.json["name"]),
        address=str(request.json["address"]),
        location=str(request.json["location"]),
        capacity=str(request.json["capacity"]),
        busyness=SmallInteger(request.json["busyness"]),
        
        # last_updated="",
    )
    db.session.add(user)

    db.session.flush()
    return str(request.json["busyness"])

@app.get("/bar")
def bar():
    # get requests can access data with request.args.get(key)
    return str(request.args.get("building"))
