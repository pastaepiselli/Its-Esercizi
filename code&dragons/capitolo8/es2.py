def pick(d: dict, keys: list[str]) -> dict:
    new_dict = {}
    for k, v in d.items():
        if k in keys:
            new_dict[k] = v
    return new_dict
            
            