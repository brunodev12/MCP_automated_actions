from web3 import Web3, EthereumTesterProvider
from eth_account.messages import encode_defunct
from data.constants import private_key_dict

w3 = Web3(EthereumTesterProvider)

def signMessageEVM(hash=None, side="bsc"):

    private_key = private_key_dict[side]

    message = encode_defunct(text=hash)

    signed_message = w3.eth.account.sign_message(
        message, private_key=private_key)

    signature = signed_message.signature.hex()

    return signature
