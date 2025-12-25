"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if len(list_one) < len(list_two) and contains(list_two, list_one):
        return SUBLIST
    if len(list_two) < len(list_one) and contains(list_one, list_two):
        return SUPERLIST
    return UNEQUAL


def contains(bigger_list, smaller_list):
    if len(smaller_list) == 0:
        return True
    for index, element in enumerate(bigger_list):
        if element == smaller_list[0] and bigger_list[index:index + len(smaller_list)] == smaller_list:
            return True
    return False