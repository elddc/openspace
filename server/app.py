from flask import Flask, request
from flask_cors import CORS  # not needed for prod
from flask_sqlalchemy import SQLAlchemy

# from sqlalchemy.orm import DeclarativeBase
import os
from dotenv import load_dotenv
import schema as model
import json
from datetime import datetime, timedelta

load_dotenv()
db = SQLAlchemy(model_class=model.Base)
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
db.init_app(app)

CORS(app)  # not needed for prod

# https://docs.sqlalchemy.org/en/20/tutorial/orm_data_manipulation.html

# Create/POST
@app.post("/new/building")
def add_building():
    # print(request.json)
    # Create a building and add it to the database
    # Database will automatically generate and add uuid for building (generated based on name?)
    building = model.Building(
        name=str(request.json["name"]),
        address=str(request.json["address"]),
        # location=str(request.json["location"]),
        capacity=str(request.json["capacity"]),
        busyness=int(request.json["busyness"]),
    )
    db.session.add(building)
    db.session.commit()
    # Set the busyness of the building and add to appropriate row of database
    # building.busyness = int(request.json["busyness"])
    # db.session.commit()

    input = model.Input(
        building_id=building.id,
        busyness=building.busyness
    )
    db.session.add(input)

    db.session.commit()

    toRet = building.busyness
    db.session.close()
    return str(toRet)

@app.post("/building")
def update_building():
    print(request.json)

    building = db.session.execute(db.select(model.Building).filter_by(name=request.json["name"])).scalar()

    # add user input
    input = model.Input(
        building_id=building.id,
        busyness=int(request.json["busyness"])
    )
    db.session.add(input)

    # caluclate the average busyness in the last 15 minutes
    filter_time = datetime.now() - timedelta(minutes=15)
    average_busyness = db.session.execute(
        db.select(db.func.avg(model.Input.busyness))
        .filter_by(building_id=building.id).filter(model.Input.time_created >= filter_time)
    ).scalar()
    print(average_busyness)
    average_busyness = int(average_busyness * 20)
    i = db.session.execute(db.select(model.Input).filter_by(building_id=building.id).filter(model.Input.time_created >= filter_time))
    for j in i:
        print(j)

    building.busyness = average_busyness
    db.session.add(building)

    db.session.commit()

    toRet = building.busyness
    db.session.close()
    return str(toRet)


@app.get("/building")
def get_building():
    if request.args.get("name"):
        return get_building_by_name(request.args.get("name"))
    return get_all_buildings()

def get_building_by_name(name):
    data = db.session.execute(
        db.select(model.Building).where(model.Building.name == name)
    ).scalar()
    return str(data.busyness)

def get_all_buildings():
    data = db.session.execute(db.select(model.Building))
    # instantiate empty list of all buildings that will be populated with dictionaries of each building
    buildings = {}
    for d in data:
        # turn d into schema.Building object
        b = d._mapping["Building"]
        # turn b into a dictionary and add to buildings
        buildings[b.name] = dict(
            id=b.id,
            name=b.name,
            address=b.address,
            location=b.location,
            capacity=b.capacity,
            busyness=b.busyness,
            last_updated=b.last_updated,
        )
    return buildings





@app.get("/room")
def get_room():
    if request.args.get("name"):
        return get_room_by_name(request.args.get("name"))
    return get_all_rooms()

def get_room_by_name(name):
    data = db.session.execute(
        db.select(model.Room).where(model.Room.name == name)
    ).scalar()
    return str(data.busyness)

def get_all_rooms():
    data = db.session.execute(db.select(model.Room))
    # instantiate empty list of all buildings that will be populated with dictionaries of each building
    rooms = list()
    for d in data:
        # turn d into schema.Building object
        b = d._mapping["Room"]
        # turn b into a dictionary
        room = dict(
            id=b.id,
            name=b.name,
            busyness=b.busyness,
            last_updated=b.last_updated,
        )
        # add building to buildings
        rooms.append(room)

    # non-JSON
    return rooms

# Doesn't work
# @app.post("/room")
# def updateRoom():
#     # db.session.add(model.Input(
#     #     name = "CIF",
#     #     busyness = request.json["busyness"],
#     # ))
#     # print(db.session.new)
#     # db.session.commit()

#     # with Session(engine) as session:
#     user = model.Room(
#         # id="",
#         name=str(request.json["name"]),
#         busyness=int(request.json["busyness"]),
#         # last_updated="",
#     )
#     db.session.add(user)

#     db.session.flush()
#     return str(request.json["busyness"])



    # JSON, UUID not JSON serializable
    # return json.dumps(buildings, indent = 4)

    # get requests can access data with request.args.get(key)
    # return str(request.args.get("building"))
