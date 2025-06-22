from mytipes import *
from persona import Persona

class PosizioneMilitare:

    _nome: str # mutabile, possibilmente noto alla nascita

    def __init__(self, nome: str) -> None:
        self.set_nome(nome)
        
    def nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str) -> None:
        if not nome:
            raise ValueError('La posizione militare non puo essere una stringa vuota')

        self._nome = nome