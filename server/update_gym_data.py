import requests
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

from db_helper import update_building

load_dotenv()
engine = create_engine(os.getenv("DB_URI"))
Session = sessionmaker(engine)


url = 'https://goboardapi.azurewebsites.net/api/FacilityCount/GetCountsByAccount?AccountAPIKey=38902ca4-0d3b-409e-903e-615e5e530612'

# List of entries of gym data
entry_list = requests.get(url).json()

# Manually view specific entry data
# for entry in entry_list:
#     if (entry['FacilityName'] == "CRCE"):
#         print(entry['FacilityName'], entry['LocationName'], entry['LastCount'], entry['TotalCapacity'])

# Find the last updated date and time using entry['LastUpdatedDateAndTime']

# Rate "Busyness" between 0-5.
# ARC and CRCE are the only gym buildings that are updated consistently on the API,
# thus ARC and CRCE are the only gym buildings that will have live updates.

# Find the last count at ARC and CRCE
ARC_COUNT = 0
CRCE_COUNT = 0

for entry in entry_list:
    if entry['FacilityName']=="ARC":
        ARC_COUNT = ARC_COUNT + int(entry['LastCount'])
    elif entry['FacilityName']=="CRCE":
        CRCE_COUNT = CRCE_COUNT + int(entry['LastCount'])

print("COUNTS: ", ARC_COUNT)
print(CRCE_COUNT)

# Find the max capacity at ARC and CRCE
ARC_CAP = 0
CRCE_CAP = 0

CRCE_LOCATIONS = ["Main Gym", "Raquetball Courts", "Squash Court", "MAC Gym", "Upper Level"]
ARC_LOCATIONS = ["Entrance Level Fitness Area", "Upper Level", "Lower Level", "Strength and Conditioning", "Gym 1", "Gym 2", "Gym 3"] 

for entry in entry_list:
    if entry['FacilityName']=="CRCE" and entry['LocationName'].strip() in CRCE_LOCATIONS:
        CRCE_CAP = CRCE_CAP + int(entry['TotalCapacity'])
    elif entry['FacilityName']=="ARC" and entry['LocationName'].strip() in ARC_LOCATIONS:
        ARC_CAP = ARC_CAP + int(entry['TotalCapacity'])

print("CAPs: ", ARC_CAP)
print(CRCE_CAP)

# Find the busyness (0-5) at ARC and CRCE
# Range: 0 to cap / 10 -> 0
# cap / 10 to 3 cap / 10 -> 1
# 3 cap / 10 to 5 cap / 10 -> 2
# ...
# 9 cap / 10 to cap -> 5
ARC_BUSYNESS = round(100 * ARC_COUNT / ARC_CAP)
CRCE_BUSYNESS = round(100 * CRCE_COUNT / CRCE_CAP)

print("BUSYNESS: ", ARC_BUSYNESS)
print(CRCE_BUSYNESS)

# Update gym data
# r = requests.post('http://127.0.0.1:5000/building', json={'name':"ARC", 'busyness': ARC_BUSYNESS})
# r = requests.post('http://127.0.0.1:5000/building', json={'name':"CRCE", 'busyness': CRCE_BUSYNESS})
# print(r)
with Session() as session:
    update_building(session, "ARC", ARC_BUSYNESS)
    update_building(session, "CRCE", CRCE_BUSYNESS)
# r = requests.get('http://127.0.0.1:5000/building', json={'name':"ARC"})
# print(r)