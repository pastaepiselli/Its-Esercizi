def frequency_dict(elements: list) -> dict:
    d  = {}
    for e in elements:
        d[e] = d.get(e, 0) + 1
    return d