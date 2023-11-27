import requests
import json

url = 'https://goboardapi.azurewebsites.net/api/FacilityCount/GetCountsByAccount?AccountAPIKey=38902ca4-0d3b-409e-903e-615e5e530612'

# List of entries of gym data
entry_list = requests.get(url).json()

# Manually view specific entry data
# for entry in entry_list:
#     if (entry['FacilityName'] == "ARC"):
#         print(entry['FacilityName'], entry['LocationName'], entry['LastUpdatedDateAndTime'])

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

print(ARC_COUNT)
print(CRCE_COUNT)

# Find the max capacity at ARC and CRCE
ARC_CAP = 0
CRCE_CAP = 0

for entry in entry_list:
    if entry['FacilityName']=="ARC":
        ARC_CAP = ARC_CAP + int(entry['TotalCapacity'])
    elif entry['FacilityName']=="CRCE":
        CRCE_CAP = CRCE_CAP + int(entry['TotalCapacity'])

print(ARC_CAP)
print(CRCE_CAP)

# Find the busyness (0-5) at ARC and CRCE
# Range: 0 to cap / 10 -> 0
# cap / 10 to 3 cap / 10 -> 1
# 3 cap / 10 to 5 cap / 10 -> 2
# ...
# 9 cap / 10 to cap -> 5
ARC_BUSYNESS = round(5 * ARC_COUNT / ARC_CAP)
CRCE_BUSYNESS = round(5 * CRCE_COUNT / CRCE_CAP)

print(ARC_BUSYNESS)
print(CRCE_BUSYNESS)

# Update gym data
r = requests.post('http://localhost:5000/building', json={'name':"ARC", 'busyness': ARC_BUSYNESS})
r = requests.post('http://localhost:5000/building', json={'name':"CRCE", 'busyness': CRCE_BUSYNESS})


# r = requests.get('http://localhost:5000/building', json={'name':"ARC"})
# print(str(r))