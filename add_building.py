import requests

def add_building(name, addr, busyness=0, capacity=-1):
    r = requests.post('http://localhost:5000/new/building', json={
        'name': name,
        'address': addr,
        'busyness': busyness,
        'capacity': capacity})
