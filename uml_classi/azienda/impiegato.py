from uml_classi.azienda.mytipes import *
from datetime import datetime


class Impiegato:

    _nome: str # mutabile
    _cognome: str # mutabile
    _nascita: datetime.date # immutabile
    _stipendio: RealGEZ # 


    def __init__(self, nome: str, cognome: str, nascita: datetime.date, stipendio: RealGEZ) -> None:

        self.set_nome(nome)
        self.set_cognome(cognome)
        self._nascita = nascita
        self.set_stipendio(stipendio)

    
    def nome(self) -> str:

        return self._nome
    
    def set_nome(self, new_name: str) -> None:

        self._nome = new_name

    def cognome(self) -> str:

        return self._cognome
    
    def set_cognome(self, new_cognome: str) -> None:

        self._cognome = new_cognome

    def nascita(self) -> datetime.date:

        return self._nascita
    
    
    def stipendio(self) -> RealGEZ:

        return self._stipendio
    
    def set_stipendio(self, new_stipendio: RealGEZ) -> None:

        self._stipendio = new_stipendio

    def __str__(self):
        
        return f'{self.nome()} {self.cognome()}, nascita: {self.nascita()} stipendio: {self.stipendio()}'
    
    def __repr__(self):
        
        pass