def sum_numbers(obj: int | float | list | tuple | dict) -> float:
    if isinstance(obj, (int, float)):
        return obj
    elif isinstance(obj,(list, tuple)):
        s = 0
        for e in obj:
            s += sum_numbers(e)
        return s
    elif isinstance(obj, (dict)):
        s = 0
        for v in obj.values():
            s += sum_numbers(v)
        return s
    else:
        return 0
        