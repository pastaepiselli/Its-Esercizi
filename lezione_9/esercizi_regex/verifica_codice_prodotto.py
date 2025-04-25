import re
def check_product_code(code: str) -> bool:

    pattern = r'PROD-[0-9]{4}-ZX'
    match = re.fullmatch(pattern, code)

    
    if match:

        return True
        
    else:
        
        return False
    
print(check_product_code("PROD-9876-ZX"))  # True
print(check_product_code("PROD-99-ZX"))    # False


