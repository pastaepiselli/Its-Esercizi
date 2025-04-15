# importo dal modulo persona.py la classe persona, quando lavoriamo con le classi 
from persona import Persona 
class Studente(Persona):

    '''
    
    attributi della classe Persona(in quanto studente eredita da persona)
    self.name
    self.lastname
    self.age

    Attributi della classe studente
    self.matricola: str
    '''
    
    # inizializzare un oggetto della classe studente

    def __init__(self, name: str, lastname: str, age: int, matricola: str):

        # inizializzare la classe persona con il metodo __init__ della superclasse
        super().__init__(name, lastname, age)

        # istruzioni che inizializzano un oggetto della classe Studente
        self.set_matricola(matricola)

    # metodo setter

    # metodo che imposta il valore dell' attributo matricola
    def set_matricola(self, matricola: str) -> None:

        if matricola:

            self.matricola = matricola
        
        else:

            print('Errore! La matricola non puo essere una stringa vuota')

    # metodo getter

    # metodo che ritorna l'attributo self.matricola

    def get_matricola(self) -> str:
        return self.matricola
    

    # overwriting // sovrascrivendo il metodo str, mi consente di avere un metodo con lo stesso nome in tutte le classi con funzioni differenti
    def __str__(self):
        super().__str__()
        return 