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


def value(colors):
    return int("".join([str(RESISTOR_COLORS.index(color)) for color in colors[:2]]))
