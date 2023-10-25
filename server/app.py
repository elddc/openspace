from flask import Flask, request
from flask_cors import CORS # not needed for prod
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import DeclarativeBase
import os
from dotenv import load_dotenv
import schema as model
import json

load_dotenv()
db = SQLAlchemy(model_class=model.Base)
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
db.init_app(app)

CORS(app) # not needed for prod

@app.post("/update")
def update():
    data = db.session.execute(
        db.select(model.Building).where(model.Building.name == request.json["name"])
    ).scalar()
    data.busyness = request.json["busyness"]
    db.session.commit()
    return str(request.json["busyness"])


@app.get("/building")
def building():
    data = db.session.execute(
        db.select(model.Building).where(model.Building.name == request.args.get("name"))
    ).scalar()
    return str(data.busyness)

@app.post("/foo")
def foo():
    # db.session.add(model.Input(
    #     name = "CIF",
    #     busyness = request.json["busyness"],
    # ))
    # print(db.session.new)
    # db.session.commit()


    # with Session(engine) as session:
    user = model.Building(
        # id="",
        name=str(request.json["name"]),
        address=str(request.json["address"]),
        location=str(request.json["location"]),
        capacity=str(request.json["capacity"]),
        busyness=int(request.json["busyness"]),

        # last_updated="",
    )
    db.session.add(user)

    db.session.flush()
    return str(request.json["busyness"])

@app.get("/bar")
def bar():
    data = db.session.execute(db.select(model.Building))
    # instantiate empty list of all buildings that will be populated with dictionaries of each building
    buildings = list()
    for d in data:
        # turn d into schema.Building object
        b = d._mapping['Building']
        # turn b into a dictionary
        building = dict(id=b.id, name=b.name, address=b.address, location=b.location, capacity=b.capacity, busyness=b.busyness, last_updated=b.last_updated)
        # add building to buildings
        buildings.append(building)
    
    # non-JSON
    return buildings
    
    # JSON, UUID not JSON serializable
    # return json.dumps(buildings, indent = 4)

    # get requests can access data with request.args.get(key)
    # return str(request.args.get("building"))
