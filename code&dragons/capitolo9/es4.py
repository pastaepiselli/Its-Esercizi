def divide_safe(a, b, default=None):
    if b == 0:
        return default
    return a / b