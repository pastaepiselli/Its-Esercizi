from datetime import date

from azienda.coinvolto import coinvolto
from azienda.impiegato import Impiegato
from custom_types import RealGEZ

class Progetto:

    _nome: str # noto alla nascita
    _budget: RealGEZ # noto alla nascita
    _impiegati: dict[Impiegato, coinvolto._link] # da associazione 'coinvolto' [0..*], certamente non noto alla nascita


    def __init__(self, nome: str, budget: RealGEZ) -> None:
        self._nome = nome
        self._budget = budget
        self._impiegati = dict()

    def nome(self) -> str:
        return self._nome

    def budget(self) -> RealGEZ:
        return self._budget

    def get_nome(self) -> str:
        return self._nome

    def get_budget(self) -> RealGEZ:
        return self._budget

    def _add_link_coinvolto(self, l: coinvolto._link) -> None:
        if l.progetto() != self:
            raise ValueError(f"Il link non coinvolge me, ma {l.progetto()}")
        if l.impiegato() in self._impiegati:
            raise KeyError(f"L'impiegato {l.impiegato()} è già coinvolto nel progetto {self.nome()}")

        self._impiegati[l.impiegato()] = l

    def _remove_link_coinvolto(self, l: coinvolto._link) -> None:
        if l.progetto() != self:
            raise ValueError(f"Il link non coinvolge me, ma {l.progetto()}")
        if l.impiegato() not in self._impiegati:
            raise KeyError(f"L'impiegato {l.impiegato().nome()} non era coinvolto nel progetto {l.progetto().nome()}")
        del self._impiegati[l.impiegato()]


    def impiegati(self) -> frozenset['coinvolto._link']:
        return frozenset(self._impiegati.values())

    def is_coinvolto(self, impiegato: Impiegato) -> bool:
        return impiegato in self._impiegati

    def data_coinvolgimento(self, impiegato: Impiegato) -> date:
        if impiegato not in self._impiegati:
            raise ValueError(f"L'impiegato non è coinvolto nel progetto {self.nome()}")
        return self._impiegati[impiegato].data()

    def __str__(self) -> str:
        return f"Progetto '{self.nome()}' con budget: {self.budget()}€"

    def __repr__(self) -> str:
        return f"Progetto(nome={self.get_nome()}, budget={self.budget()})"