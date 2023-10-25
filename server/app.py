from flask import Flask, request
from flask_cors import CORS # not needed for prod
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import DeclarativeBase
import os
from dotenv import load_dotenv
import schema as model

load_dotenv()
db = SQLAlchemy(model_class=model.Base)
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
db.init_app(app)

CORS(app) # not needed for prod

# https://docs.sqlalchemy.org/en/20/tutorial/orm_data_manipulation.html

# Create/POST
# Needs review
@app.post("/building")
def post():
    # print(request.json)
    # Create a building and add it to the database
    # Database will automatically generate and add uuid for building (generated based on name?)
    building = model.Building(
        name=str(request.json["name"]),
        address=str(request.json["address"]),
        location=str(request.json["location"]),
        capacity=str(request.json["capacity"]),
        busyness=int(request.json["busyness"]),
        # name="test",
        # busyness=3,
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
   
    return str(building.busyness)


# Read/GET
@app.get("/get")
def get():
    data = db.session.execute(db.select(model.Building))
    for d in data:
        print(d)

    # get requests can access data with request.args.get(key)
    return str(request.args.get("building"))


# Update/PATCH
# Needs review
@app.put("/building")
def patch():
    building = db.session.execute(db.select(model.Building).filter_by(name=request.json["name"])).scalar()
    building.busyness = int(request.json["busyness"])
    db.session.add(building)
    db.session.commit()
    
    input = model.Input(
        building_id=building.id,
        busyness=building.busyness
    )
    db.session.add(input)
    
    db.session.commit()

    return building.name



# Delete/DELETE
# Needs review
@app.delete("/delete")
def delete():
    building = db.session.execute(db.select(model.Building).filter_by(name=request.json["name"])).scalar()
    db.session.delete(building)
    db.session.commit()


# Needed for page to load ?!
@app.get("/building")
def building():
    data = db.session.execute(
        db.select(model.Building).where(model.Building.name == request.args.get("name"))
    ).scalar()
    return str(data.busyness)


'''
NOTES:
    Access data with request.json[key]
    e.g. to access "busyness" from server, use request.json["busyness"]


    # db.session.add(model.Building(
    # db.session.add(model.Input(
    #     name = "CIF",
    #     busyness = request.json["busyness"],
    # ))
    # print(db.session.new)
    # db.session.commit()
'''