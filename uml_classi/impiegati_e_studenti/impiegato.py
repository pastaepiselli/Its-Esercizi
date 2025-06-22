from mytipes import *
from persona import Persona
from datetime import datetime
from progetto import Progetto
from resp_progetto import resp_progetto

class Impiegato(Persona):

    _stipendio: RealGEZ # mutabile, noto alla nascita
    _ruolo: Ruolo # mutabile noto alla nascita  
    _is_responsabile: bool # mutabile, probabilmente non noto alla nasita [0..1]
    _progetti_responabile: dict[Progetto, resp_progetto] # certamente non noto alla nascita non noto alla nascita

    def __init__(self,nome: str, cognome: str, cf: CodiceFiscale, nascita: datetime.date, genere: Genere,\
         stipendio: RealGEZ, ruolo: Ruolo, is_responsabile: bool) -> None:

        super().__init__(nome, cognome, cf, nascita, genere)
        self.set_stipendio(stipendio)
        self.set_ruolo(ruolo)
        self.set_is_responsabile(is_responsabile)

        if ruolo == ruolo.progettista:
            self._progetti_responabile = dict()

    # STIPENDIO

    def stipendio(self) -> RealGEZ: 
        return self._stipendio

    def set_stipendio(self, stipendio: RealGEZ) -> None:
        self._stipendio = stipendio
    

    # RUOLO

    def ruolo(self) -> Ruolo:
        return self._ruolo
    
    def set_ruolo(self, ruolo: Ruolo) -> None:
        if ruolo is None:
            raise ValueError('Il ruolo non puo essere lasciato vuoto')
        
        self._ruolo = ruolo
    
    # IS_RESPONSABILE

    def is_responsabile(self) -> bool:
        return self._is_responsabile

    def set_is_responsabile(self, is_responsabile: bool) -> None:
        self._is_responsabile = is_responsabile

    # LINK RESP_PROG

    def _add_link_resp_prog(self, l: resp_progetto) -> None:
        if l.impiegato() != self:
            raise ValueError(f"Il link non coinvolge me, ma {l.impiegato()}")
        if l.progetto() in self._progetti_responabile:
            raise KeyError(f"L'impiegato è già coinvolto nel progetto {l.progetto()}")
        self._progetti_responabile[l.progetto()] = l

    def _remove_link_resp_prog(self, l: resp_progetto) -> None:
        if l.impiegato() != self:
            raise ValueError(f"Il link non coinvolge me, ma {l.impiegato()}")
        if l.progetto() not in self._progetti_responabile:
            raise KeyError(f"L'impiegato {self.nome()} non era coinvolto nel progetto {l.progetto()}")
        del self._progetti_responabile[l.progetto()]

    def progetti(self) -> frozenset[resp_progetto]:
        return frozenset(self._progetti_responabile.values())

    def is_coinvolto(self, progetto: Progetto) -> bool:
        return progetto in self._progetti_responabile

