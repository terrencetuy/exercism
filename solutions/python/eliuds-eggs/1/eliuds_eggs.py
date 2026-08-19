def egg_count(display_value):
    egg_count = 0
    while display_value > 0:
        if display_value % 2 == 1:
            egg_count += 1
        display_value //= 2   
    return egg_count
