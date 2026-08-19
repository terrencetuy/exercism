def line_up(name, number):
    return f"{name}, you are the {to_ordinal(number)} customer we serve today. Thank you!"


def to_ordinal(number):
    return str(number) + get_suffix(number)

    
def get_suffix(number):
    if 11 <= number % 100 <= 13:
        return "th"
        
    match number % 10:
        case 1:
            return "st"
        case 2:
            return "nd"
        case 3:
            return "rd"
    return "th"