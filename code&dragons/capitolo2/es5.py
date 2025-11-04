def deep_get(d: dict | list, path: list, default=None):
    strada = d
    for k in path:
        try:
           strada = strada[k]
        except Exception:
            return default
    return strada