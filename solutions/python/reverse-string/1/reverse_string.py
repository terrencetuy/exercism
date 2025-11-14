def reverse(text):
    if len(text) <= 1:
        return text
    return text[-1] + reverse(text[0:len(text)-1])
