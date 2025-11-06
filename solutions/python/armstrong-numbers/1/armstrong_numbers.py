def is_armstrong_number(number: int) -> bool:
    digits = to_digits(number)
    number_of_digits = len(digits)
    return sum([digit ** number_of_digits for digit in digits]) == number
  
def to_digits(number: int) -> list[int]:
    digits = []
    while number > 0:
        digits.append(number % 10)
        number //= 10
    return digits