from impiegato import Impiegato
from mytipes import *
from progetto import Progetto

class resp_progetto:

    @classmethod
    def add(cls, progetto: Progetto, impiegato: Impiegato) -> _link:
        l = cls._link(progetto, impiegato)
        progetto._add_link_coinvolto(l)
        impiegato._add_link_coinvolto(l)
        return l # restituisco il link appena creato, per comodità di utilizzo

    @classmethod
    def remove(cls, l: _link) -> None:
        l.progetto()._remove_link_coinvolto(l)
        l.impiegato()._remove_link_coinvolto(l)
        del l   # devo cancellare il link

    class _link:

        _impiegato: Impiegato # immutabile, noto alla nascita
        _progetto: Progetto # immutabile, noto alla nascita

        def __init__(self, impiegato: Impiegato, progetto: Progetto) -> None:

            self._impiegato = impiegato
            self._progetto = progetto

        def impiegato(self) -> Impiegato:
            return self._impiegato

        def progetto(self) -> Progetto:
            return self._progetto


    
