def intersection_sorted(a: list[int], b: list[int]) -> list[int]:
    a = set(a)
    b = set(b)
    return sorted(list(a & b))