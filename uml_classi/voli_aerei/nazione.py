class Nazione:

    _nome: str # mutabile noto alla nascita

    def __init__(self, nome: str):
        
        self.set_nome(nome)

    def nome(self) -> str:

        return self._nome
    
    def set_nome(self, nome: str) -> None:

        self._nome = nome