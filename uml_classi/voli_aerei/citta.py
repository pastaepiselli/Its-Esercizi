from mytypes import IntGEZ

class Citta:

    _nome: str # mutabile
    _n_abitanti: IntGEZ # mutabile

    def __init__(self, nome: str, abitanti: IntGEZ):
        self.set_nome(nome)
        self.set_n_abitanti(abitanti)

    def nome(self) -> str:

        return self._nome

    def set_nome(self, nome: str) -> None:

        self._nome = nome

    def n_abitanti(self) -> IntGEZ:

        return self._n_abitanti
    
    def set_n_abitanti(self, abitanti: IntGEZ) -> None:

        self._n_abitanti = abitanti

    