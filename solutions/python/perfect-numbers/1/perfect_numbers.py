def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    factors = [factor for factor in range(1, number) if number % factor == 0]
    alloquot_sum = sum(factors)
    
    if alloquot_sum == number:
        return "perfect"
    if alloquot_sum < number:
        return "deficient"
    return "abundant"
