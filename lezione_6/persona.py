class Persona:
    # di una persona dobbiamo sapere delle informazioni
    # queste informazioni vengono chiamate attributi
    # __init__ e il costruttore della classe persona 
    def __init__(self, nome: str, cognome: str, eta: int):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    # funzione che fa parte della classe persona che usa self
    def display_data(self):
        print(f'Name: {ln.nome}, LastName: {ln.cognome}, age: {ln.eta}') 


        
ln = Persona('lorenzo', 'rossi', 19) # stampa la posizione in memoria

print(f'Name: {ln.nome}, LastName: {ln.cognome}, age: {ln.eta}') # con il punto va ad estrarre la variabile no posso mosrate in putput tutto insietet

ln.display_data()