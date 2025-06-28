from mytipes import *
from datetime import datetime
from __future__ import annotations

class Persona:

    _nome: str # mutabile, noto alla nascita
    _cognome: str # mutabile, noto alla nascita
    _cf: CodiceFiscale # mutabile, noto alla nascita
    _nascita: datetime.date # immutabile, noto alla nascita
    _maternita: IntGEZ # mutabile, certamente non noto alla nascita, se valorizzato genere = donna
    _genere: Genere # mutabile, noto alla nascita


    def __init__(self, nome: str, cognome: str, cf: CodiceFiscale, nascita: datetime.date, maternita: IntGEZ = None, genere: Genere) -> None:

        pass

    # NOME

    def nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str) -> None:
        self._nome = nome

    # COGNOME

    def cognome(self) -> str:
        return self._cognome

    def set_cognome(self, cognome: str) -> None:
        self._cognome = cognome

    # CODICE FISCALE

    def cf(self) -> CodiceFiscale:
        return self._cf

    def set_cf(self, cf: CodiceFiscale) -> None:
        self._cf = cf

    # NASCITA SOLO GET

    def nascita(self) -> datetime.date:
        return self._nascita

    # GENERE

    def genere(self) -> Genere:
        return self._genere

    def set_genere(self, genere: Genere) -> None
        # se una donna cambia sesso tiene le maternita???   
        if genere == genere.uomo:
            self._maternita = None


    # MATERNITA

    def maternita(self) -> IntGEZ:
        return self._maternita

    def add_maternita(self) -> None:
        if self.genere() = genere.donna:


    
