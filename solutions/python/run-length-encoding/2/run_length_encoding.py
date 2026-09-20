import re

def decode(string):
    return ''.join([
        expand(chunk) for chunk in re.findall(r'[0-9]*[A-Za-z\s]', string)
    ])


def expand(string):
    if len(string) == 1:
        return string
    return string[-1] * int(string[:-1])


def encode(string):
    if len(string) == 0:
        return ''
        
    count = 0
    current_character = string[0]
    for character in string:
        if not character == current_character:
            break
        count += 1
    encoded_section = str(count) + current_character if count > 1 else current_character

    return encoded_section + encode(string[count:])

    
 
