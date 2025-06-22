from mytipes import *
from impiegato import Impiegato
from resp_progetto import resp_progetto

class Progetto:

    _nome: str # mutabile, noto alla nascita
    _responsabili: dict[Impiegato, resp_progetto]

    def __init__(self, nome: str) -> None:

        self.set_nome(nome)
        self._responsabili = dict()

    def nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str) -> None:

        if not nome: 
            raise ValueError('Il nome del progetto non puo essere una stringa vuota')

        self._nome = nome

    
    # LINK RESP_PROG

    def _add_link_resp_prog(self, l: resp_progetto._link) -> None:
        if l.progetto() != self:
            raise ValueError(f"Il link non appartiene a questo progetto: {l.progetto()}")
        if l in self._responsabili:
            raise KeyError(f"Il responsabile è già assegnato a questo progetto.")
        self._responsabili.add(l)

    def _remove_link_resp_prog(self, l: resp_progetto._link) -> None:
        if l.progetto() != self:
            raise ValueError(f"Il link non appartiene a questo progetto: {l.progetto()}")
        if l not in self._responsabili:
            raise KeyError(f"Il link non è presente in questo progetto.")
        self._responsabili.remove(l)

    def responsabili(self) -> frozenset[resp_progetto]:
        return frozenset(self._responsabili.values())

