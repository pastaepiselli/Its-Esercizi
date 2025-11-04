def is_valid_record(x: dict | list | str | None) -> bool:
    if isinstance(x, dict):
        return True
    return False