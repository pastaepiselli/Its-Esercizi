import re
def is_valid_name(name: str) -> bool:

    pattern = r'[A-Z][a-z]{2,}'

    match = re.fullmatch(pattern, name)

    if match:

        return True
    
    else:

        return False


print(is_valid_name("Marco"))  # True
print(is_valid_name("marco"))  # False
print(is_valid_name("Ma"))      # False

