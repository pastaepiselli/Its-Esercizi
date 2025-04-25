def create_contact(nome_cognome: str, email: str = None, telefono: int = None) -> dict:

    contact: dict[str:str, int] = {'profile': nome_cognome, 'email': email, 'telefono': telefono}
    return contact

def update_contact(dictionary: dict, name: str, email: str = None, telefono: int=None) -> dict:
    
    dictionary['profile'] = name
    if email:

        dictionary['email'] = email

    if telefono:

        dictionary['telefono'] = telefono

    return dictionary
        



