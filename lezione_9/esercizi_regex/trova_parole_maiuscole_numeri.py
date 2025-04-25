import re 

def find_codes(text: str) -> list[str]:

    pattern = r'[A-Z0-9]{8}'

    match = re.findall(pattern, text)

    return match

print(find_codes('I codici sono AB12CD34 e 12345678 e XYZZYZZZ'))