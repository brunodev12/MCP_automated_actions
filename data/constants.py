import os
import random
from utils.tron_to_eth import tronToEth

address_dict = {
    "trx": tronToEth(os.environ.get('ADDRESS_TRON')),
    "eth": os.environ.get('ADDRESS_ETH'),
    "bsc": os.environ.get('ADDRESS_BSC')
}

private_key_dict = {
    "eth": os.environ.get('PRIVATE_KEY_ETH'),
    "bsc": os.environ.get('PRIVATE_KEY_BSC')
}

idx_dict = {
    "trx": random.randint(10000000, 99999999),
    "eth": random.randint(10000000, 99999999),
    "bsc": random.randint(10000000, 99999999)
}