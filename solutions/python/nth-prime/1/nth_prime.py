def prime(number):
    if number == 0:
        raise ValueError("there is no zeroth prime")
        
    primes = [2]
    while len(primes) < number:
        primes.append(get_next_prime(primes))
    return primes[-1]

def get_next_prime(primes):
    number_to_check = primes[-1]
    while True:
        number_to_check += 1
        if is_next_prime(number_to_check, primes):
            return number_to_check
        

def is_next_prime(to_check, primes):
    for prime in primes:
        if to_check % prime == 0:
            return False
    return True