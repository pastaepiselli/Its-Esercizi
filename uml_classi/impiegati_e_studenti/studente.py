from persona import Persona
from mytipes import *

class Studente(Persona):

    _matricola: IntGZ # immutabile, noto alla nascita

    def __init__(self, nome: str, cognome: str, cf: CodiceFiscale, nascita: datetime.date, genere: Genere, matricola: IntGZ) -> None:

        super().__init__(nome, cognome, cf, nascita, genere)
        self._matricola = matricola 

    # MATRICOLA
    
    def matricola(self) -> IntGZ:
        return self._matricola




