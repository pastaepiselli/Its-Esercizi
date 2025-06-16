# import re

# def is_valid_ipv4(address: str) -> bool:

#     pattern = r'(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}'

#     if re.fullmatch(pattern, address):
#         return True


#     return False



print(is_valid_ipv4("192.168.0.1"))
print(is_valid_ipv4("255.255.255.255"))
print(is_valid_ipv4("256.100.10.1"))


# correzione esercizio

def check_ipv4(address: str) -> bool:
    # crea la lista senza i punti
    address = address.split(".")

    if len(address) != 4:
        return False
    
    for elem in address:
        # nel ciclo for faccio 2 controlli
        if not elem.isdigit():
            # raise ValueError('Errore indirizzo contiene una stringa ... inserire solo numeri')
            return False

        if not 0 <= int(elem) <= 255:
            # raise ValueError('')
            return False
            


    return True