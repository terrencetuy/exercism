def square_root(number):
    guess = number
    while not guess * guess == number:
        guess = (guess + number / guess) / 2
    return guess
    
