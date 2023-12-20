import json
from sign_message_tron import signMessageTron
from sign_message_evm import signMessageEVM

with open("hash_list.json") as jsonfile:
    hash_list = json.load(jsonfile)

sign_message_list = []

for i in hash_list:
    hash = i[0]
    side = i[1]

    if hash is not None:
        if side == "trx":
            sign_message = signMessageTron(hash)
        else:
            sign_message = signMessageEVM(hash, side)

        sign_message_list.append([hash, sign_message, side])

with open("sign_message_list.json", "w") as jsonfile:
    json.dump(sign_message_list, jsonfile)
