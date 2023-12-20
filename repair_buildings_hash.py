import csv
import json
from actionsMCP.entry_point import getMessageRepair, getTxHashRepair
from data.constants import address_dict
import os

building_list = []

for filename in os.listdir('.'):
    if filename.endswith('.csv'):
        csv_file = filename
        break

with open(csv_file, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        building_list.append(row)

with open("idx.json") as jsonfile:
    idx_dict = json.load(jsonfile)

with open("building_info.json") as jsonfile:
    building_info = json.load(jsonfile)

print("=======================BUILDING INFO========================")
for i in building_info:
    print(i)

hash_list = []

print("======================READY TO REPAIR=======================")
for i, j in zip(building_info, building_list):
    token_id = i['tokenId']

    condition = 100
    set_condition = 0
    if token_id == j['Token id']:
        condition = int(i['condition'])
        set_condition = int(j['Repair when conditions is X'])

    side = 'trx'
    message = None
    if (condition < 100 and set_condition != 0) and (condition <= set_condition):
        side = j['Network']
        address = address_dict[side]
        idx = idx_dict[side]
        message = getMessageRepair(side, idx, token_id, address)

    if message is not None:
        hash = getTxHashRepair(message, side)
        hash_list.append([hash, side])
        print(hash, "token id:", token_id)


with open("hash_list.json", "w") as jsonfile:
    json.dump(hash_list, jsonfile)
