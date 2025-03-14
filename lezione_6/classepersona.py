from typing import Any
class Admin:

    def __init__(self):
        pass







class Persona: # stampino per la creazione di persona

    def __init__(self, nome, cognome, eta): # funzione costruttore
        # self e una variabile che contiene un indirizzo di memoria
        self.nome = nome # la variabile self permette di specificare a quale istanza mi sto riferendo
        self.cognome = cognome
        self.eta = eta
        self.passwords = "passwords" # in questo caso non e un parametro che cambia ma e sempre uguale per tutte le istanze

    def get_nome(self): # e un getter e viene usato per schermare le variabili della classe da utenti esterni (usati anche i setter) 
        
        return self.nome    
    
    def set_name(self, nome): # il setter e lunica cosa che possiamo utilizzare per cambiare in nome quando e privato 

        self.__nome = nome # con l'underscore la variabile diventa privata

    def get_password(self, tipo: Any):

        if type(tipo) == Admin: # in questo caso chi ha la classe admin puo accedere alla password  

            return self.passwords
        
        raise ValueError("Non puoi accedere alla password")

    def set_password(self):

        raise ValueError("Non puoi modificare la password")
    








persona_1: Persona = Persona("Mario", "Rossi", 30)
persona_2: Persona = Persona("Flavio", "Rossi", 31)
persona_3: Persona = Persona("Flavio", "Mori", 31)       
persona_4: Persona = Persona("Flavio", "Mori", 31)    
    

persona_1.nome
persona_2.nome