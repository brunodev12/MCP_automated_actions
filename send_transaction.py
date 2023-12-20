import json
import os
from actionsMCP.entry_point import sendTx
from tron_to_eth import tronToEth

address_dict = {
    "trx": tronToEth(os.environ.get('ADDRESS_TRON')),
    "eth": os.environ.get('ADDRESS_ETH'),
    "bsc": os.environ.get('ADDRESS_BSC')
}

with open("sign_message_list.json") as jsonfile:
    sign_message_list = json.load(jsonfile)

for i in sign_message_list:
    hash = i[0]
    sign_message = i[1]
    side = i[2]
    address = address_dict[side]
    sendTx(address, hash, sign_message, side)
