import requests
import json

url = 'https://goboardapi.azurewebsites.net/api/FacilityCount/GetCountsByAccount?AccountAPIKey=38902ca4-0d3b-409e-903e-615e5e530612'

# produces a list of entry(s) (which have different tags)
entry_list = requests.get(url).json()


for entry in entry_list:
    if (entry['FacilityName'] == "ARC"):
        print(entry['FacilityName'], entry['LocationName'], entry['LastUpdatedDateAndTime'])


CRCE_CAP = 0
ARC_CAP = 0
ICEARENA_CAP = 0
OUTDOORCENTER_CAP = 0
COMPLEXFIELDS_CAP = 0

for entry in entry_list:
    if entry['FacilityName']=="CRCE":
        CRCE_CAP = CRCE_CAP + int(entry['MaxCapacityRange'])
    elif entry['FacilityName']=="ARC":
        ARC_CAP = ARC_CAP + int(entry['MaxCapacityRange'])
    elif entry['FacilityName']=="Ice Arena":
        ICEARENA_CAP = ICEARENA_CAP + int(entry['MaxCapacityRange'])
    elif entry['FacilityName']=="Outdoor Center Play Fields":
        OUTDOORCENTER_CAP = OUTDOORCENTER_CAP + int(entry['MaxCapacityRange'])
    elif entry['FacilityName']=="Complex Fields":
        COMPLEXFIELDS_CAP = COMPLEXFIELDS_CAP + int(entry['MaxCapacityRange'])


# Used for adding gym buildings
# r = requests.post('http://localhost:5000/new/building', json={'name':"ARC", 'address':'201 E Peabody Dr, Champaign, IL 61820', 'busyness': 0, 'capacity':ARC_CAP})
# r = requests.post('http://localhost:5000/new/building', json={'name':"CRCE", 'address':'1102 W Gregory Dr, Urbana, IL 61801', 'busyness': 0, 'capacity':CRCE_CAP})
# r = requests.post('http://localhost:5000/new/building', json={'name':"Ice Arena", 'address':'406 E Armory Ave, Champaign, IL 61820', 'busyness': 0, 'capacity':ICEARENA_CAP})
# r = requests.post('http://localhost:5000/new/building', json={'name':"Outdoor Center Play Fields", 'address':'1201 S Dorner Dr, Urbana, IL 61801', 'busyness': 0, 'capacity':OUTDOORCENTER_CAP})
# r = requests.post('http://localhost:5000/new/building', json={'name':"Complex Fields", 'address':'1201 W Florida Ave, Urbana, IL 61801', 'busyness': 0, 'capacity':COMPLEXFIELDS_CAP})



ARC_BUSYNESS = 0
CRCE_BUSYNESS = 0

for entry in entry_list:
    if entry['FacilityName']=="CRCE":
        CRCE_BUSYNESS = CRCE_BUSYNESS + int(entry['LastCount'])
    elif entry['FacilityName']=="ARC":
        ARC_BUSYNESS = ARC_BUSYNESS + int(entry['LastCount'])

print(ARC_BUSYNESS)
print(CRCE_BUSYNESS)

# r = requests.post('http://localhost:5000/new/building', json={'name':"ARC", 'address':'201 E Peabody Dr, Champaign, IL 61820', 'busyness': 0, 'capacity':ARC_CAP})