def slices(series, length):
    series_length = len(series)
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if series_length == 0:
        raise ValueError("series cannot be empty")
    if series_length < length:
        raise ValueError("slice length cannot be greater than series length")

    return [
        series[index:index+length] 
        for index in range(series_length - length + 1)
    ]
