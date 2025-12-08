def append(list1, list2):
    return list1 + list2


def concat(lists):
    if len(lists) == 0:
        return []
    return  lists[0] + concat(lists[1:])


def filter(function, list):
    return [item for item in list if function(item)]
    

def length(list):
    return len(list)


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    if len(list) == 0:        
        return initial
    return foldl(function, list[1:], function(initial, list[0]))


def foldr(function, list, initial):
    if len(list) == 0:        
        return initial
    item = list.pop()
    return foldr(function, list, function(initial, item))


def reverse(list):
    if len(list) == 0:
        return []
    return [list.pop()] + reverse(list)
        
