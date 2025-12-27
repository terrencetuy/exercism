import math

def find(search_list, value):
    if len(search_list) == 0:
        raise ValueError("value not in array")

    if len(search_list) == 1:
        if search_list[0] == value:
            return 0
        raise ValueError("value not in array")

    middle_index = math.ceil(len(search_list)/2)
    if value > search_list[middle_index - 1]:
        return find(search_list[middle_index:], value) + middle_index 
    return find(search_list[0:middle_index], value) 
