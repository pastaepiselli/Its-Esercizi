from mytypes import *

class Aeroporto:

    _codice: CodiceAeroporto # mutabile
    _nome: str # mutabile

    def __init__(self, codice: CodiceAeroporto, nome: str) -> None:

        self.set_codice(codice)
        self.set_nome(nome)

        

    def codice(self) -> CodiceAeroporto:

        return self._codice
    
    def set_codice(self, codice: CodiceAeroporto) -> None:

        self._codice = codice

    def nome(self) -> str:

        return self._nome
    
    def set_nome(self, nome: str) -> None:

        self._nome = nome
        
        
        

    