from flask import Flask, request
from flask_cors import CORS # not needed for prod
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
import schema as model

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
    for d in data:
        print(d)

    # get requests can access data with request.args.get(key)
    return str(request.args.get("building"))
