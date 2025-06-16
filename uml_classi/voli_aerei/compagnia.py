from __future__ import annotations
from mytypes import *
from citta import Citta
from volo import *
from volo_comp import *

class Compagnia:

    _nome: str # mutabile, noto alla nascita
    _annoFondazione: Int1900 # immutabile, noto alla nascita
    _sede: Citta # mutabile, conosciuto dalla nascita
    _voli: set[VoloComp] #  da assoc. volo_comp [0..*], certamente non noti alla nascita
    
    def __init__(self, nome: str, annofondazione: Int1900, sede: Citta) -> None:
        self.set_nome(nome)
        self._annoFondazione = annofondazione
        self._sede = sede
        self._voli = set() 


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

    def  __str__(self) -> str:
        return f'Nome compagnia: {self.nome()} con anno di fondazione {self.annoFondazione()} e sede a {self.sede().nome()}'