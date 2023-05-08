import csv
import json
from actionsMCP.entry_point import getLandData, getMessageRepair, getTxHashRepair
from tron_to_eth import tronToEth
import random
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

address_dict = {
    "trx": tronToEth(os.environ.get('ADDRESS_TRON')),
    "eth": os.environ.get('ADDRESS_ETH'),
    "bsc": os.environ.get('ADDRESS_BSC')
}

idx_dict = {
    "trx": random.randint(10000000, 99999999),
    "eth": random.randint(10000000, 99999999),
    "bsc": random.randint(10000000, 99999999)
}

building_info = []

for i in building_list:
    # print(i['Token id'], i['X'], i['Y'], i['Collect every X days'], i['Repair when conditions is X'], i['Speed up'], i['Network'])
    side = i['Network']
    data = getLandData(i['X'], i['Y'], side)
    building_info.append({'tokenId': data['token_id'], 'lastAction': data['last_action'], 'lastSpeedUp': data['last_speed_up'],
                         'usages': data['building_stat']['usages'], 'condition': data['condition'], 'buildingId': data['building_id'], 'actionId': data['action_id'], 'citizens': data['citizens']})

with open("building_info.json", "w") as jsonfile:
    json.dump(building_info, jsonfile)

hash_list = []

for i, j in zip(building_info, building_list):
    token_id = i['tokenId']
    if token_id == j['Token id']:
        condition = int(i['condition'])
        set_condition = int(j['Repair when conditions is X'])
        if condition < 100 and set_condition != 0:
            if (condition <= set_condition):

                side = j['Network']
                address = address_dict[side]
                idx = idx_dict[side]

                message = getMessageRepair(side, idx, token_id, address)

                if message is not None:
                    hash = getTxHashRepair(message, side)
                    hash_list.append([hash, side])
                    print(hash)


with open("hash_list.json", "w") as jsonfile:
    json.dump(hash_list, jsonfile)
