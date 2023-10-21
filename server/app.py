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

@app.post("/foo")
def foo():
    # CREATE
    
    # db.session.add(model.Building(
    #     name = "CIF",
    #     address = "1405 W. Springfield",
    #     busyness = request.json["busyness"],
    # ))
    # print(db.session.new)
    # db.session.commit()

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
        # name=str(request.json["name"]),
        # address=str(request.json["address"]),
        # location=str(request.json["location"]),
        # capacity=str(request.json["capacity"]),
        # busyness= int(request.json["busyness"]),
        name="andrew",
        busyness=3

        # last_updated="",
    )
    db.session.add(user)
    print(user.id)
    db.session.commit()
    print(user.id)
    input = model.Input(
        busyness= int(request.json["busyness"])
    )
    db.session.add(input)
    db.session.commit()
    return str(request.json["busyness"])

# UPDATE: get object name, update as shown above (input)

@app.get("/bar")
def bar():
    data = db.session.execute(db.select(model.Building))
    print(data)

    # get requests can access data with request.args.get(key)
    return str(request.args.get("building"))
