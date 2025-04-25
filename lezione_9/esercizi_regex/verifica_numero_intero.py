import re
def is_integer(s: str) -> bool:

    return bool(re.fullmatch(r'[+ | -]?\d+', s))
 
    
print(is_integer('-45.0'))    

    