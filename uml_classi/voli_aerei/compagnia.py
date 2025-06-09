from __future__ import annotations
from mytypes import *
from citta import Citta
from volo import *

class Compagnia:

    _nome: str # mutabile, noto alla nascita
    _annoFondazione: Int1900 # immutabile, noto alla nascita
    _sede: Citta # mutabile, conosciuto dalla nascita
    _voli: set[Volo]

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
    
    def _add_volo(self, volo: Volo) -> None:

        self._voli.add(volo)

    def remove_volo(self, volo: Volo) -> None:

        self._voli.remove(volo)

    def voli(self) -> frozenset[Volo]:

        return frozenset(self._voli)