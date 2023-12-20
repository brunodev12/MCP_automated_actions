import json
import os
from actionsMCP.entry_point import sendTx
from data.constants import address_dict

with open("sign_message_list.json") as jsonfile:
    sign_message_list = json.load(jsonfile)

for i in sign_message_list:
    hash = i[0]
    sign_message = i[1]
    side = i[2]
    address = address_dict[side]
    sendTx(address, hash, sign_message, side)
