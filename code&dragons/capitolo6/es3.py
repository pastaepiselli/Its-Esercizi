def safe_div(a: float, b: float, default=None):
    if b == 0:
        return default
    return a / b

    