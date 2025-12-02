def flatten(iterable):
    flattened = []
    for item in iterable:
        if isinstance(item, list):
            flattened += flatten(item)
        elif item is not None:
            flattened.append(item)
        
    return flattened
