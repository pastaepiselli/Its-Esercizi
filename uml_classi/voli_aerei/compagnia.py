from mytypes import *
from citta import Citta

class Compagnia:

    _nome: str # mutabile
    _annoFondazione: Int1900 # immutabile
    _sede: Citta # mutabile, conosciuto dalla nascita

    def __init__(self, nome: str, annofondazione: Int1900, sede: Citta) -> None:
        self.set_nome(nome)
        self._annoFondazione = annofondazione
        self._sede = sede


    def nome(self) -> str:

        return self._nome
    
    def set_nome(self, n: str) -> None:

        self._nome = n

    def annoFondazione(self) -> Int1900:

        return self._annoFondazione
    
    def sede(self) -> Citta:

        return self._sede
    
    def set_sede(self, sede: Citta) -> None:

        self._sede = sede