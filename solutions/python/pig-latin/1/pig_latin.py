VOWELS = ["a", "e", "i", "o", "u"]


def translate(text):
    return " ".join([rotate_word(word) + "ay" for word in text.split(" ")])


def rotate_word(word):
    if word[0] in VOWELS or word[0:2] in ["xr", "yt"]:
        return word
        
    index = 0
    while (word[index] == "y" and index == 0) or word[index] not in VOWELS + ["y"] or (word[index-1] == "q" and word[index] == "u"):
        index += 1

    return word[index:] + word[0:index]
    
