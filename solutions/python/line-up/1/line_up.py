def line_up(name, number):
    return f"{name}, you are the {to_ordinal(number)} customer we serve today. Thank you!"


def to_ordinal(number):
    return str(number) + get_suffix(number)

    
def get_suffix(number):
    mod10 = number % 10
    mod100 = number % 100
    
    if mod10 == 1 and mod100 != 11:
        return "st"
    if mod10 == 2 and mod100 != 12:
        return "nd"
    if mod10 == 3 and mod100 != 13:
        return "rd"
    return "th"