def get_or_default(d: dict, k, default=None):
    if k in d:
        return d[k]
    return default