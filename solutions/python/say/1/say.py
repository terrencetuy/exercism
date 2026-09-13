def say(number):
    if not 0 <= number < 1_000_000_000_000:
        raise ValueError("input out of range")

    if number == 0:
        return "zero"

    number_words = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",  
    }

    number_words_tens= {
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety",
    }

    powers_of_ten = {
        1_000_000_000: "billion",
        1_000_000: "million",
        1_000: "thousand",
        100: "hundred"
    }

    for power, power_as_word in powers_of_ten.items():
        if number >= power:
            quotient, remainder = divmod(number, power)
            number_as_words = say(quotient) + f" {power_as_word}"
            if remainder > 0:
                number_as_words += " " + say(remainder)
            return number_as_words
        
    if number >= 20:
        tens_word = number_words_tens[number // 10]
        if number % 10 > 0:
            return "-".join([tens_word, number_words[number % 10] ])
        return tens_word
    
    if number in number_words.keys():
        return number_words[number]


