import csv
import json
from actionsMCP.entry_point import getLandData, getMessageCollect, getTxHashCollect
from tron_to_eth import tronToEth
import random
import time
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

with open("idx.json", "w") as jsonfile:
    json.dump(idx_dict, jsonfile)

building_info = []

for i in building_list:
    # print(i['Token id'], i['X'], i['Y'], i['Collect every X days'], i['Repair when conditions is X'], i['Speed up'], i['Network'])
    side = i['Network']
    address = address_dict[side]
    data = getLandData(i['X'], i['Y'], side, address)
    if data is not None:
        building_info.append({'tokenId': data['token_id'], 'lastAction': data['last_action'], 'lastSpeedUp': data['last_speed_up'],
                         'usages': data['building_stat']['usages'], 'condition': data['condition'], 'buildingId': data['building_id'], 'actionId': data['action_id'], 'citizens': data['citizens']})

with open("building_info.json", "w") as jsonfile:
    json.dump(building_info, jsonfile)

print("=======================BUILDING INFO========================")
for i in building_info:
    print(i)

hash_list = []

print("======================READY TO COLLECT======================")
actual_time = int(time.time())
for i, j in zip(building_info, building_list):
    token_id = i['tokenId']
    if token_id == j['Token id']:
        days_in_seconds = int(j['Collect every X days']) * 86400
        if days_in_seconds != 0 and i['citizens'] is not None:
            speed_up = j['Speed up'] == "yes"
            side = j['Network']
            address = address_dict[side]
            idx = idx_dict[side]
            if (actual_time - int(i['lastAction']) > days_in_seconds):

                message = getMessageCollect(address, side, idx, speed_up,
                                     token_id, i['buildingId'], i['actionId'])
                

                if message is not None:
                    daysLeft = int(message['values'][4])
                    if daysLeft == 0:
                        hash = getTxHashCollect(message, side)
                        hash_list.append([hash, side])
                        print(hash, "token id:", token_id)
                    elif speed_up:
                        lastSpeedUp = i['lastSpeedUp']
                        last_speed_up = time.mktime(time.strptime(
                            lastSpeedUp, "%Y-%m-%dT%H:%M:%S.%fZ")) if lastSpeedUp is not None else 0
                        if actual_time - int(last_speed_up) > 86400:
                            
                            message = getMessageCollect(address, side, idx, speed_up,
                                                    token_id, i['buildingId'], i['actionId'])
                            hash = getTxHashCollect(message, side)
                            hash_list.append([hash, side])
                            print(hash, "token id:", token_id)

with open("hash_list.json", "w") as jsonfile:
    json.dump(hash_list, jsonfile)
