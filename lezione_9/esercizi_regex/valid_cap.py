import re
def valid_cap(cap: str) -> bool:

    pattern =r'[0-9]{5}'

    match = bool(re.fullmatch(pattern, cap))
    if match:

        return True
        
    else:
        
        return False

print(valid_cap('000544'))