class Citta:

    _nome: str

    def __init__(self, nome: str):

        self._nome = nome

    def nome(self) -> str:

        return self._nome
    
    def set_nome(self, n: str) -> None:

        self._nome = n
        
