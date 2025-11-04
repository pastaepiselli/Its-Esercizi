def invert_unique(d: dict) -> dict:
    new_dict = {}
    for k, v in d.items():
        new_dict[v] = k
    return new_dict