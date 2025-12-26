ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def encode(plain_text):
    return chunk(transcode(plain_text.lower(), ALPHABET, ALPHABET[::-1]))


def decode(ciphered_text):
    return transcode(ciphered_text, ALPHABET[::-1], ALPHABET)


def transcode(text, source_chars, cipher_chars):
    return "".join(
        transcode_letter(letter, source_chars, cipher_chars) 
        for letter in text
    )


def transcode_letter(letter, source_chars, cipher_chars):
    if not letter.isalnum():
        return ""       
    if letter in source_chars:
        index = source_chars.index(letter)
        return cipher_chars[index]       
    return letter

    
def chunk(text, chunk_size=5):
    return " ".join(
        text[index: index + chunk_size] 
        for index in range(0, len(text), chunk_size)
    )
