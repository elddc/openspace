import requests
import json

url = 'https://goboardapi.azurewebsites.net/api/FacilityCount/GetCountsByAccount?AccountAPIKey=38902ca4-0d3b-409e-903e-615e5e530612'

# produces a list of entry(s) (which have different tags)
entry_list = requests.get(url).json()


for entry in entry_list:
    print(entry['FacilityName'], entry['LocationName'], entry['MaxCapacityRange'])

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


r = requests.post('http://127.0.0.1:5000/new/building', data={'name':"ARC", 'capacity':ARC_CAP})
r = requests.post('http://127.0.0.1:5000/new/building', data={'name':"CRCE", 'capacity':CRCE_CAP})
r = requests.post('http://127.0.0.1:5000/new/building', data={'name':"Ice Arena", 'capacity':ICEARENA_CAP})
r = requests.post('http://127.0.0.1:5000/new/building', data={'name':"Outdoor Center Play Fields", 'capacity':OUTDOORCENTER_CAP})
r = requests.post('http://127.0.0.1:5000/new/building', data={'name':"Complex Fields", 'capacity':COMPLEXFIELDS_CAP})
