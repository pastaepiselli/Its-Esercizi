from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from azienda.coinvolto import coinvolto
    from azienda.progetto import Progetto
from custom_types import RealGEZ

from datetime import date

class Impiegato:
    _nome: str # noto alla nascita
    _cognome: str # noto alla nascita
    _nascita: date # <<immutable>>, # noto alla nascita
    _stipendio: RealGEZ # # noto alla nascita

    _progetti: dict['Progetto', 'coinvolto._link'] # da associazione 'coinvolto' [0..*], certamente non noto alla nascita

    def __init__(self, nome:str, cognome:str, nascita: date, stipendio: RealGEZ) -> None:
        self.set_nome(nome)
        self.set_cognome(cognome)
        self._nascita = nascita
        self.set_stipendio(stipendio)
        self._progetti = dict() # perché è certamente non noto alla nascita

    def nome(self) -> str:
        return self._nome

    def cognome(self) -> str:
        return self._cognome

    def nascita(self) -> date:
        return self._nascita

    def stipendio(self) -> RealGEZ:
        return self._stipendio

    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def set_cognome(self, cognome: str) -> None:
        self._cognome = cognome

    def set_stipendio(self, stipendio: RealGEZ) -> None:
        self._stipendio = stipendio

    def _add_link_coinvolto(self, l: 'coinvolto._link') -> None:
        if l.impiegato() != self:
            raise ValueError(f"Il link non coinvolge me, ma {l.impiegato()}")
        if l.progetto() in self._progetti:
            raise KeyError(f"L'impiegato è già coinvolto nel progetto {l.progetto()}")
        self._progetti[l.progetto()] = l

    def _remove_link_coinvolto(self, l: 'coinvolto._link') -> None:
        if l.impiegato() != self:
            raise ValueError(f"Il link non coinvolge me, ma {l.impiegato()}")
        if l.progetto() not in self._progetti:
            raise KeyError(f"L'impiegato {self.nome()} non era coinvolto nel progetto {l.progetto()}")
        del self._progetti[l.progetto()]

    def progetti(self) -> frozenset['coinvolto._link']:
        return frozenset(self._progetti.values())

    def is_coinvolto(self, progetto: 'Progetto') -> bool:
        return progetto in self._progetti

    def data_coinvolgimento(self, progetto: 'Progetto') -> date:
        if progetto not in self._progetti:
            raise ValueError(f"L'impiegato non è coinvolto nel progetto {progetto.nome()}")
        return self._progetti[progetto].data()

    def __str__(self) -> str:
        return (f"{self.nome()} {self.cognome()}, "
                f"nascita: {self.nascita()}, "
                f"stipendio: {self.stipendio()}")
