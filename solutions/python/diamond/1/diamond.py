def rows(letter):
    ascii_value = ord(letter)
    lines = [
        "".join(get_padding(i, ascii_value) + get_middle(chr(i)) + get_padding(i, ascii_value)) 
        for i in range(65, ascii_value + 1)
    ]
    return lines + lines[-2::-1]

def get_padding(start, stop):
    return [" " for j in range(start, stop)]

def get_middle(letter):
    spaces = (ord(letter) - 65) * 2 - 1

    if spaces < 1:
        return [letter]
    return [letter] + [" " for j in range(spaces)] + [letter]