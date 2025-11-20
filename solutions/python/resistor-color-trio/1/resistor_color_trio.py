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


def label(colors):
    resistance_value = int("".join([str(RESISTOR_COLORS.index(color)) for color in colors[:2]])) * 10 ** RESISTOR_COLORS.index(colors[2])
    label = "0 ohms"
    for index, prefix in enumerate(prefixes):
        prefix_value = 10 ** (3 * index)
        if resistance_value >= prefix_value:
            label = f"{resistance_value // prefix_value} {prefix}ohms"
    return label
