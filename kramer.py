__all__ = ['paquet', 'routingDec2Hex']

def paquet(_in, _out):
    return b'\x01' + \
        routingDec2Hex(_in) + \
        routingDec2Hex(_out) + \
        b'\x81'

def routingDec2Hex(num):
    assert num in range(1,17)
    return bytes([num + 128])