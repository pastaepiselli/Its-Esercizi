from __future__ import annotations

class Specie:

    nome: str
    popolazione: int
    tasso_crescita: float

    def __init__(self, nome: str, popolazione: int ,tasso_crescita: float) -> None:

        self.nome = nome
        self.popolazione = popolazione
        self.tasso_crescita = tasso_crescita
        
    def cresci(self) -> int:
        popolazione_nuova = self.popolazione * (1 + self.tasso_crescita / 100)
        self.popolazione = popolazione_nuova
        return popolazione_nuova

    def getDensita(self, area_kmq: float) -> int:
        
        densita = self.popolazione / area_kmq
        anni = 1

        while densita != 1:
            self.cresci()
            densita = self.popolazione / area_kmq

        return anni

    def anni_per_superare(self, altra_specie: Specie) -> int:
        anni = 0
        if self.popolazione > altra_specie.popolazione:
            print(f'La popolazione dei {self.nome} e gia maggiore del {altra_specie.nome}')
            return anni

        while self.popolazione < altra_specie.popolazione:
            self.cresci()
            anni += 1

        return anni

    
class BufaloKlingon(Specie):

    def __init__(self,nome: str, popolazione: int, tasso_crescita: float) -> None:
        super().__init__(nome, popolazione, tasso_crescita)
        self.nome = "Bufalo Klingon"

class Elefante(Specie):

    def __init__(self,nome: str, popolazione: int, tasso_crescita: float) -> None:
        super().__init__(nome, popolazione, tasso_crescita)
        self.nome = "Elefante"


            

