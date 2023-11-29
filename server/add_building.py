import requests
import schema as model
from sqlalchemy import select

def add_building(name, addr, busyness=0, capacity=-1):
    r = requests.post('http://localhost:5000/new/building', json={
        'name': name,
        'address': addr,
        'busyness': busyness,
        'capacity': capacity})

def update_building(Session, building_name, new_busyness):
    toRet = -1
    with Session.begin() as session:
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