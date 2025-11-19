def is_valid(isbn):
    isbn = list(isbn.replace("-", ""))
    isbn_length = len(isbn)
    if not isbn_length == 10:
        return False
    if isbn[-1] == "X":
        isbn[-1] = "10"
    if not all([number.isdigit() for number in isbn]):
        return False
        
    isbn_sum = sum([int(digit) * (isbn_length - i) for i, digit in enumerate(isbn)])
    return isbn_sum % 11 == 0
