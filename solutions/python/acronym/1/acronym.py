def abbreviate(words):
    punctuation = '_*.!:;'
    return "".join([
        word.strip(punctuation)[0].upper() 
        for word in words.replace('-', ' ').split()
    ])
