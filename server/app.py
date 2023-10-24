from flask import Flask, request
from flask_cors import CORS # not needed for prod
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import DeclarativeBase
import os
from dotenv import load_dotenv
import schema as model

# from datetime import datetime   # --> Added to support post method
# now = datetime.now()            # --> Added to support post method

load_dotenv()
db = SQLAlchemy(model_class=model.Base)
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
db.init_app(app)

CORS(app) # not needed for prod


# Create/POST
# NEEDS FIXING (?)
@app.post("/post")
def post():
    user = model.Building(
        #name=str(request.json["name"]),
        #address=str(request.json["address"]),
        #location=str(request.json["location"]),
        #capacity=str(request.json["capacity"]),
        #busyness=int(request.json["busyness"]),
        name="Andrew",
        busyness=3,
        # last_updated=now    # --> I can't seem to add add user to the database without setting this....
    )
    db.session.add(user)
    print(user.id)
    db.session.commit()
    print(user.id)
    #input = model.Input(
    #    busyness= int(request.json["busyness"])
    #)
    #db.session.add(input)
    #db.session.commit()
    return str(request.json["busyness"])


# Read/GET
@app.get("/get")
def get():
    data = db.session.execute(db.select(model.Building))
    for d in data:
        print(d)

    # get requests can access data with request.args.get(key)
    return str(request.args.get("building"))


# Update/PATCH
# NEEDS FIXING (?)
@app.patch("/patch")
def patch():
    data = db.session.execute(
        db.select(model.Building).where(model.Building.name == request.json["name"])
    ).scalar()
    data.busyness = request.json["busyness"]
    db.session.commit()
    # print(data.name)
    return str(request.json["busyness"])


# Update/PUT
# NEEDS FIXING (?)
@app.put("/put")
def put():
    user = model.Building(
        #name=str(request.json["name"]),
        #address=str(request.json["address"]),
        #location=str(request.json["location"]),
        #capacity=str(request.json["capacity"]),
        #busyness=int(request.json["busyness"]),
        name="Andrew",
        busyness=3,
        last_updated=now    # --> I can't seem to add add user to the database without setting this....
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


# Delete/DELETE
# TO BE IMPLEMENTED (?)


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