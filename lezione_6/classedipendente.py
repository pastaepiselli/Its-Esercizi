from classepersona import Persona




class Dipendente(Persona):
    
    def __init__(self, nome, cognome, eta, stipendio):
        super().__init__(nome, cognome, eta)
        self.stipendio = stipendio

    def get_stipendio(self, stipendio):

        return stipendio
