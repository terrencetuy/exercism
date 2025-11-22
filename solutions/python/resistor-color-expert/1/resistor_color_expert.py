RESISTOR_COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white"
]

prefixes = [
    "",
    "kilo",
    "mega",
    "giga"
]

RESISTOR_TOLERANCES = {
    "grey": "0.05",
    "violet": "0.1",
    "blue": "0.25",
    "green": "0.5",
    "brown": "1",
    "red": "2",
    "gold": "5",
    "silver": "10"
}


def resistor_label(colors):   
    if len(colors) == 1:
        return "0 ohms"

    tolerance = colors.pop()
    multiplier = colors.pop()

    resistance_value = int("".join([str(RESISTOR_COLORS.index(color)) for color in colors])) * 10 ** RESISTOR_COLORS.index(multiplier)
    label = "0 ohms"
    for index, prefix in enumerate(prefixes):
        prefix_value = 10 ** (3 * index)
        if resistance_value >= prefix_value:
            if resistance_value % prefix_value == 0:
                label = f"{resistance_value // prefix_value} {prefix}ohms"
            else:
                label = f"{resistance_value / prefix_value} {prefix}ohms"
    
    return f"{label} ±{RESISTOR_TOLERANCES[tolerance]}%"
