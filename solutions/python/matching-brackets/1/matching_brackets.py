OPENERS = {
    "]": "[",
    "}": "{",
    ")": "("
}


def is_paired(input_string):
    brackets = []
    for char in input_string:
        if char in OPENERS.values():
            brackets.append(char)

        if char in OPENERS.keys():
            if len(brackets) == 0 or brackets[-1] is not OPENERS[char]:
                return False
            brackets.pop()

    return len(brackets) == 0