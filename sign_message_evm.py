from web3 import Web3, EthereumTesterProvider
from eth_account.messages import encode_defunct
import os

w3 = Web3(EthereumTesterProvider)

private_key_dict = {
    "eth": os.environ.get('PRIVATE_KEY_ETH'),
    "bsc": os.environ.get('PRIVATE_KEY_BSC')
}


def signMessageEVM(hash=None, side="eth"):

    private_key = private_key_dict[side]

    message = encode_defunct(text=hash)

    signed_message = w3.eth.account.sign_message(
        message, private_key=private_key)

    signature = signed_message.signature.hex()

    return signature
