import requests
import schema as model
from sqlalchemy import select

def create_building(session, name, addr, busyness=0, capacity=-1):
    # print(request.json)
    # Create a building and add it to the database
    # Database will automatically generate and add uuid for building (generated based on name?)
    building = model.Building(
        name = name,
        address = addr,
        busyness = busyness,
        capacity = capacity
    )
    session.add(building)
    session.commit()
    # Set the busyness of the building and add to appropriate row of database
    # building.busyness = int(request.json["busyness"])
    # session.commit()

    input = model.Input(
        building_id=building.id,
        busyness=building.busyness
    )
    session.add(input)

    session.commit()

    toRet = building.busyness
    return str(toRet)

def update_building(session, building_name, new_busyness):
    toRet = -1
    building = session.execute(select(model.Building).filter_by(name=building_name)).scalar()
    building.busyness = new_busyness
    session.add(building)
    session.commit()

    input = model.Input(
        building_id=building.id,
        busyness=building.busyness
    )
    session.add(input)

    session.commit()

    toRet = building.busyness
    return str(toRet)