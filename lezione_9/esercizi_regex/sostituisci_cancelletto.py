import re
def mask_numbers(text: str) -> str:

    pattern = r'[0-9]+'

    match = str(re.sub(pattern, '###', text))
    
    
    return match

print(mask_numbers('Il codice è 12345 e la data è 2025.'))
    
