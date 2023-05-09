import base58

def tronToEth(address):
    if address is not None:
        if not address.startswith('0x') and not address.startswith('0X'):
            asc_string = base58.b58decode_check(address)
            return asc_string.hex().upper().replace("41","0X")
    return address