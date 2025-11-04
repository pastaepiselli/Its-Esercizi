def to_int(x, default=0):
    try:
        x = int(x)
        return x
    except Exception:
        return default
    