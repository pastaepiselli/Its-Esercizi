from mytipes import *
from datetime import datetime, date
from Posizione_militare import PosizioneMilitare

class Persona:
    _nome: str # mutabile, noto alla nascita
    _cognome: str # mutabile, noto alla nascita
    _cf: CodiceFiscale # mutabile, noto alla nascita
    _nascita: datetime.date # immutabile, noto alla nascita
    _maternita: IntGEZ # mutabile, probabilmente non noto alla nascita
    _genere: Genere # mutabile, noto alla nascita
    _posizione_militare: PosizioneMilitare # mutabile

    def __init__(self, *, nome: str, cognome: str, cf: CodiceFiscale, nascita: datetime.date, genere: Genere, posizione_militare: PosizioneMilitare = None) -> None:
        # questi dati verranno cambiati
        
        self._maternita = None
        self._genere = None

        self.set_nome(nome)
        self.set_cognome(cognome)
        self.set_cf(cf)
        self._nascita = nascita
        self.set_genere(genere, posizione_militare=posizione_militare)
        

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, nome: str) -> None:
        self._nome = nome
    
    def cognome(self) -> str:
        return self._cognome

    def set_cognome(self, cognome: str) -> None:
        self._cognome = cognome
    
    def cf(self) -> CodiceFiscale:
        return self._cf

    def set_cf(self, cf: CodiceFiscale) -> None:
        self._cf = cf

    def nascita(self) -> datetime:
        return self._nascita

    def maternita(self) -> IntGEZ | None:
        if self.genere() == Genere.uomo:
            raise ValueError('Un uomo non puo avere maternita')

        return self._maternita

    def add_maternita(self) -> None:
        if self.genere() == Genere.uomo:
            raise ValueError('Un uomo non puo aggiungere maternita')

        self._maternita += 1

    def genere(self) -> Genere:
        return self._genere

    def set_genere(self, genere, posizione_militare: PosizioneMilitare = None) -> None:

        if genere == Genere.uomo:
            if self.genere() == Genere.uomo:
                print('Il genere gia e impostato a uomo')
                return
            self._genere = genere
            self.set_posizione_militare(posizione_militare)
            self._maternita = None
    
        elif genere == Genere.donna:
            if self.genere() == Genere.donna:
                print('Il genere gia e impostato a donna')
                return
            self._genere = genere
            self._maternita = 0
            self.set_posizione_militare(None)

    def posizione_militare(self) -> str:
        # ritorno il nome della posizione
        return self._posizione_militare.nome()


    def set_posizione_militare(self, posizione: PosizioneMilitare) -> None:
        # imposto come un attributo la classe posizione militare
        if self.genere() == Genere.donna and posizione is not None:
            raise ValueError('Le donne non possono avere una posizione militare')
        self._posizione_militare = posizione


        
