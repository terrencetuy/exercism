def factors(value):
    if value == 1:
        return []
        
    for i in range(2, value+1):
        if value % i == 0:
            return [i] + factors(value // i)
