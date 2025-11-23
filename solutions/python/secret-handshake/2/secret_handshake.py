ACTIONS = ["wink", "double blink", "close your eyes", "jump", "reverse actions"]


def commands(binary_str):
    binary_int = int(binary_str)
    handshake = []
    for i in range(0, 4):
        if binary_int % 2 == 1:
            handshake.append(ACTIONS[i])
        binary_int //= 10

    if binary_int % 2 == 1:
        handshake.reverse()
        
    return handshake
