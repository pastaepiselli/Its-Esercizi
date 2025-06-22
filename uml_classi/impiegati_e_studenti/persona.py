from mytipes import *
from datetime import datetime
from posizione_militare import PosizioneMilitare

class Persona:

    _nome: str # mutabile, noto alla nascita
    _cognome: str # mutabile, noto alla nascita
    _cf: CodiceFiscale # mutabile, noto alla nascita
    _nascita: datetime.date # immutabile, noto alla nascita
    _maternita: IntGEZ # mutabile, certamente non noto alla nascita [0..1]
    _genere: Genere # mutabile, noto alla nascita
    _posizione_militare: PosizioneMilitare # mutabile, non noto alla nascita


    def __init__(self, nome: str, cognome: str, cf: CodiceFiscale, nascita: datetime.date, genere: Genere):

        self.set_nome(nome)
        self.set_cognome(cognome)
        self.set_cf(cf)
        self._nascita = nascita # impostato senza set poiche immutabile
        self.set_genere(genere)

    # NOME 

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome: str) -> None:
        if not nome:
            raise ValueError('Il nome non puo essere una stringa vuota')

        self._nome = nome

    # COGNOME

    def cognome(self) -> str:
        return self._cognome 

    def set_cognome(self, cognome: str) -> None:
        if not cognome:
            raise ValueError('Il cognome non puo essere una stringa vuota')
        
        self._cognome = cognome

    # CODICE FISCALE

    def cf(self) -> CodiceFiscale:
        return self._cf

    def set_cf(self, cf: CodiceFiscale) -> None:

        if not cf:
            raise ValueError('Il codice fiscale non puo essere una strina vuota')

        self._cf = cf

    # NASCITA SOLO GET

    def nascita(self) -> datetime.date:
        return self._nascita

    # GENERE
    
    def genere(self) -> Genere:
        return self._genere

    def set_genere(self, genere: Genere) -> None:
        if not genere:
            raise ValueError('Il genere non puo essere lasciato vuoto')

        self._genere = genere        




        