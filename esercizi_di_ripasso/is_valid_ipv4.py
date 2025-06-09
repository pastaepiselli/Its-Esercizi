import re

def is_valid_ipv4(address: str) -> bool:

    pattern = r'(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}'

    if re.fullmatch(pattern, address):
        return True


    return False



print(is_valid_ipv4("192.168.0.1"))
print(is_valid_ipv4("255.255.255.255"))
print(is_valid_ipv4("256.100.10.1"))