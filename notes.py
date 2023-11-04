"""
============ IMPORTANT ROOMS ============
Ice Arena Ice Rink
ARC Upper Level
CRCE Main Gym 
ARC Lower Level
Ice Arena Stick and Puck
CRCE Indoor Pool
ARC Strength and Conditioning
ARC Indoor Pool
CRCE Raquetball Courts
CRCE MP 1
ARC Outdoor Pool
CRCE MP 2
CRCE Squash Court
ARC Combat Room
CRCE MAC Gym
ARC Gym 1 
CRCE Upper Level 
ARC Gym 2 
ARC Gym 3 
ARC Rock Wall
ARC Raquetball Courts
ARC Squash Courts
ARC MP Room 1
ARC MP Room 2
ARC MP Room 3
ARC MP Room  4 
ARC MP Room 5
ARC MP Room 6 
ARC MP Room 7
Outdoor Center Play Fields ODC  North Turf Fields 
Outdoor Center Play Fields ODC South Turf Fields 
Outdoor Center Play Fields ODC North Basketball Courts 
Outdoor Center Play Fields ODC South Basketball Courts
Outdoor Center Play Fields ODC Sand Volleyball Courts
Outdoor Center Play Fields ODC Tennis Courts 
Complex Fields Complex Softball Fields 
Complex Fields Complex Grass Fields

============ OTHER ROOMS ============
ARC Entrance Level Fitness Area 
CRCE Lobby Area
Ice Arena Ice Arena Lobby
CRCE Hot Tub
ARC Sauna

============ FACILITIES ============
ARC
CRCE
Ice Arena
Outdoor Center
Complex Fields
"""

%pip install requests

import requests
import json

url = 'https://goboardapi.azurewebsites.net/api/FacilityCount/GetCountsByAccount?AccountAPIKey=38902ca4-0d3b-409e-903e-615e5e530612'

entry_list = requests.get(url).json()

std::vector<std::string> buildings{"ARC, CRCE, Ice Arena, Outdoor Center, Complex Fields"};
std::vector<std::pair<int, int>> size_

std::map<std::string, std::pair<int, int>> buildings;
for (std::string building : buildings) {
    int size = 0;
    int capacity = 0;

    for entry in entry_list:
        size += entry[LastCount];
        capacity += entry[TotalCapacity];
}


for entry in entry_list:
    print(entry['FacilityName'], entry['LocationName'])