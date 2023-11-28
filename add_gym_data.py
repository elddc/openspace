import requests
import json

url = 'https://goboardapi.azurewebsites.net/api/FacilityCount/GetCountsByAccount?AccountAPIKey=38902ca4-0d3b-409e-903e-615e5e530612'

# List of entries of gym data
entry_list = requests.get(url).json()

# Manually view specific entry data
for entry in entry_list:
    if (entry['FacilityName'] == "ARC"):
        print(entry['FacilityName'], entry['LocationName'], entry['LastCount'], entry['TotalCapacity'])


# Find the max capacity of each gym facility
CRCE_CAP = 0
ARC_CAP = 0
ICEARENA_CAP = 0
OUTDOORCENTER_CAP = 0
COMPLEXFIELDS_CAP = 0

CRCE_LOCATIONS = ["Main Gym", "Raquetball Courts", "Squash Court", "MAC Gym", "Upper Level"]
ARC_LOCATIONS = ["Entrance Level Fitness Area", "Upper Level", "Lower Level", "Strength and Conditioning", "Gym 1", "Gym 2", "Gym 3"] 

for entry in entry_list:
    if entry['FacilityName']=="CRCE" and entry['LocationName'].strip() in CRCE_LOCATIONS:
        CRCE_CAP = CRCE_CAP + int(entry['TotalCapacity'])
    elif entry['FacilityName']=="ARC" and entry['LocationName'].strip() in ARC_LOCATIONS:
        ARC_CAP = ARC_CAP + int(entry['TotalCapacity'])
    elif entry['FacilityName']=="Ice Arena":
        ICEARENA_CAP = ICEARENA_CAP + int(entry['TotalCapacity'])
    elif entry['FacilityName']=="Outdoor Center Play Fields":
        OUTDOORCENTER_CAP = OUTDOORCENTER_CAP + int(entry['TotalCapacity'])
    elif entry['FacilityName']=="Complex Fields":
        COMPLEXFIELDS_CAP = COMPLEXFIELDS_CAP + int(entry['TotalCapacity'])


print(CRCE_CAP)
print(ARC_CAP)
print(ICEARENA_CAP)
print(OUTDOORCENTER_CAP)
print(COMPLEXFIELDS_CAP)


# Add gym buildings
# r = requests.post('http://127.0.0.1:5000/new/building', json={'name':"ARC", 'address':'201 E Peabody Dr, Champaign, IL 61820', 'busyness': 0, 'capacity':ARC_CAP})
# r = requests.post('http://127.0.0.1:5000/new/building', json={'name':"CRCE", 'address':'1102 W Gregory Dr, Urbana, IL 61801', 'busyness': 0, 'capacity':CRCE_CAP})
# r = requests.post('http://127.0.0.1:5000/new/building', json={'name':"Ice Arena", 'address':'406 E Armory Ave, Champaign, IL 61820', 'busyness': 0, 'capacity':ICEARENA_CAP})
# r = requests.post('http://127.0.0.1:5000/new/building', json={'name':"Outdoor Center Play Fields", 'address':'1201 S Dorner Dr, Urbana, IL 61801', 'busyness': 0, 'capacity':OUTDOORCENTER_CAP})
# r = requests.post('http://127.0.0.1:5000/new/building', json={'name':"Complex Fields", 'address':'1201 W Florida Ave, Urbana, IL 61801', 'busyness': 0, 'capacity':COMPLEXFIELDS_CAP})

# print(r)