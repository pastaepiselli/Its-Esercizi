from __future__ import annotations
from datetime import date
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from azienda.impiegato import Impiegato
    from azienda.progetto import Progetto

class coinvolto:
    # e una classe factory non ha oggetti propri serve solo a creare e cancellare oggetti della classe interna _link
    @classmethod
    def add(cls, progetto: Progetto, impiegato: Impiegato, data: date) -> _link:
        l = cls._link(progetto, impiegato, data)
        progetto._add_link_coinvolto(l)
        impiegato._add_link_coinvolto(l)
        return l # restituisco il link appena creato, per comodità di utilizzo

    @classmethod
    def remove(cls, l: _link) -> None:
        l.progetto()._remove_link_coinvolto(l)
        l.impiegato()._remove_link_coinvolto(l)
        del l   # devo cancellare il link

    class _link:

        _impiegato: 'Impiegato'     # ovviamente immutabile, noto alla nascita
        _progetto: 'Progetto'       # ovviamente immutabile, noto alla nascita
        _data: date                 # immutabile, noto alla nascita

        def __init__(self, progetto: Progetto, impiegato: Impiegato,
                     data: date) -> None:
            self._impiegato = impiegato
            self._progetto = progetto
            self._data = data

        def impiegato(self) -> 'Impiegato':
            return self._impiegato

        def progetto(self) -> 'Progetto':
            return self._progetto

        def data(self) -> date:
            return self._data

        def __hash__(self) -> int:
            return hash((self.impiegato(), self.progetto()))

        def __eq__(self, other: Any) -> bool:
            if type(other) != type(self) \
                or hash(self) != hash(other):
                return False
            return (self.impiegato(), self.progetto()) == (other.impiegato(), other.progetto())