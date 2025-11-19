def rotate(text, key):
    return "".join([rotate_char(char, key) for char in text])

def rotate_char(char, key):
    ascii_value = ord(char)
    offset = 0
    if 65 <= ascii_value <= 90:
        offset = 65
    if 97 <= ascii_value <= 122:
        offset = 97

    if offset > 0:
        return chr(offset + (ascii_value - offset + key) % 26)
    return char