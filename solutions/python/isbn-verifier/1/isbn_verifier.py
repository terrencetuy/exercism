def is_valid(isbn):
    isbn = isbn.replace("-", "")

    if not (len(isbn) == 10 and isbn[0:9].isdigit() and (isbn[9].isdigit() or isbn[9] == "X")):
        return False
        
    isbn_sum = 0
    for index in range(0, 9):
        isbn_sum += int(isbn[index]) * (10 - index)
    if isbn[9].isdigit():
        isbn_sum += int(isbn[9])
    if isbn[9] == "X":
        isbn_sum += 10

    return isbn_sum % 11 == 0
