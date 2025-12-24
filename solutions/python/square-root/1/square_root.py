def square_root(number):
    guess = number
    while not guess ** 2 == number:
        guess = (guess + number / guess) / 2
    return guess
    
