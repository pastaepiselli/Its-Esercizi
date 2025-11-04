def sum_above_threshold(numbers: list[int], tr: int) -> int:
    s = 0
    for n in numbers:
        if n > tr:
            s += n 
    return s