def commands(binary_str):
    binary_int = int(binary_str, 2)
    actions = ["jump", "close your eyes", "double blink", "wink"]
    handshake = []
    
    while len(actions) > 0:
        action = actions.pop()
        if binary_int & 1:
            handshake.append(action)
        binary_int >>= 1

    if binary_int & 1:
        handshake.reverse()
    
    return handshake
