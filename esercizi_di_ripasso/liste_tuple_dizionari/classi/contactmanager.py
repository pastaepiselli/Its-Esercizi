class ContactManager:

    def __init__(self):

        self.contacts: dict[str, list[str]] = {}

    
    def create_contact(self, name: str, phone_numbers: list[str]) -> None:

        """
        Crea un contatto e ritorna un dizionario con i valori appena creati
        """

        if name in self.contacts:
            raise ValueError('Errore, il contatto esiste gia')
        
        else:
            self.contacts[name] = phone_numbers
            return {name: phone_numbers}

    def add_phone_number(self, contact_name: str, phone_number: str) -> dict[str, list[str]]:

        """
        Aggiunge un numero
        di telefono al contatto specificato. Restituisce un nuovo dizionario con il solo
        contatto aggiornato
        """
        if contact_name not in self.contacts:
            raise ValueError('Il contatto non esiste!')

        if phone_number in self.contacts[contact_name]:
            raise ValueError('Il numero gia e associato al conttato')

        self.contacts[contact_name].append(phone_number)
        return {contact_name: self.contacts[contact_name]}

    def remove_phone_number(self, contact_name: str, phone_number: str) -> dict[str: list[str]]:

        """
        Rimuove un
        numero di telefono dal contatto specificato. Restituisce un nuovo dizionario con il
        solo contatto aggiornato
        """
        if contact_name not in self.contacts:
            raise ValueError('Il contatto non esiste')
        
        if phone_number not in self.contacts[contact_name]:
            raise ValueError('Il numero di telefono non e presente')

        self.contacts[contact_name].remove(phone_number)
        return {contact_name: self.contacts[contact_name]}

    
    def update_phone_number(contact_name: str, old_number_number: str, new_phone_number: str) -> dict[str, list[str]]:

        if contact_name not in self.contacts:

            raise ValueError('Il contatto non esiste!')

        if phone_number not in self.contacts[contact_name]:
            raise ValueError('Il numero non e presente')

        self.contacts[contact_name].index(old_number_number)
        self.contacts[contact_name][index] = new_phone_number
        return {contact_name: self.contacts[contact_name]}


    def list_contacts(self) -> list[str]:
        
        return list(self.contacts.keys())

    def list_phone_numbers(contact_name: str) -> list[str]:

        if contact_name not in self.contacts:
            raise ValueError('Contatto non presente')

        return self.contacts[contact_name]

    def search_contact_by_phone_number(self, phone_number: str) -> list[str]:
        contact_list: list[str] = []
        for contacts, list_contacts in self.contacts.items():

            if phone_number in list_contacts:

                contact_list.append(contacts)
        if  contact_list == []:
            raise Exception('Nessun contratto trovato con questo numero di telefonop')
        return contact_list
              





        
                




        

    
