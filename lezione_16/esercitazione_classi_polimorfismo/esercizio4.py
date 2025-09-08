from __future__ import annotations

class Specie:

    def __init__(self, nome: str, popolazione: int, tasso_crescita: float) -> None:

        self._nome = nome
        self._popolazione = popolazione
        self._tasso_crescita = tasso_crescita

    # metodi get
    def nome(self) -> str:
        return self._nome

    def popolazione(self) -> int:
        return self._popolazione

    def tasso_crescita(self) -> float:
        return self._tasso_crescita

    # questo metodo lo faccio per resettare la popolazione per fare il secondo test
    # def reset_pop(self) -> None:
    #     if self.nome() == 'Bufalo Klingon':
    #         self._popolazione = 100
    #     self._popolazione = 10
            
    # metodi 
    def cresci(self, popolazione: int) -> None: # inserisco popolazione in input solo perche lo richiede la traccia
        # la popolazione non serve inserita in input perche e un attributo della classe
        self._popolazione *= (1 + self._tasso_crescita / 100)

    def anni_per_superare(self, altra_specie: Specie) -> int | str:
        anni = 1
        pop_self = self.popolazione()
        pop_altra = altra_specie.popolazione()
        # nel caso gia fosse piu grande
        if self.popolazione() >= altra_specie.popolazione():
            return f'La popolazione dei {self.nome} e gia piu grande di quella dei {altra_specie.nome()}'

        while True:
            # faccio passare un anno con il metodo cresci
            pop_self = pop_self * (1 + self.tasso_crescita() / 100)
            pop_altra = pop_altra * (1 + altra_specie.tasso_crescita() / 100)
            anni +=  1
            if pop_self >= pop_altra:
                return anni

    def getDensita(self, area_kmq: float) -> int | str:
        # nel caso gia fosse 1 
        anni = 0 
        pop = self.popolazione()    
        densita = int(pop / area_kmq)

        if densita >= 1:
            return f'La densita di popolazione della specie {self.nome()} e gia di un individuo per km2'
        
        while True:
            # aumento la popolazione e ricalcolo la densita
            pop = int(pop * (1 + self.tasso_crescita() / 100))
            densita = pop / area_kmq
            anni += 1

            if densita >= 1:
                return anni
            
            if anni == 1000:
                return '1000+'
                


class BufaloKlingon(Specie):

    def __init__(self, popolazione: int, tasso_crescita: float) -> None:

        super().__init__('Bufalo Klingon',popolazione, tasso_crescita)
            
class Elefante(Specie):

    def __init__(self,popolazione: int, tasso_crescita: float) -> None:

        super().__init__('Elefante', popolazione, tasso_crescita)


