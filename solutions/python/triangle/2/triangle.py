def equilateral(sides: list[int]) -> bool:
    return triangle(sides) and len(set(sides)) == 1


def isosceles(sides: list[int]) -> bool:
    return triangle(sides) and len(set(sides)) < 3


def scalene(sides: list[int]) -> bool:
    return triangle(sides) and len(set(sides)) == 3


def triangle(sides: list[int]) -> bool:
    sorted_sides = sorted(sides)
    return sorted_sides[0] > 0 and sorted_sides[0] + sorted_sides[1] >= sorted_sides[2]