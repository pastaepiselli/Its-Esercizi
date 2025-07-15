class Contatore:

    conteggio: int

    def __init__(self) -> None:
        self.conteggio = 0

    def setZero(self) -> None:
        self.conteggio = 0

    def add1(self) -> None:
        self.conteggio += 1

    def sub1(self) -> None:
        if self.conteggio == 0:
            print('Non è possibile eseguire la sottrazione')
            return
        self.conteggio -= 1

    def get(self) -> int:
        return self.conteggio

    def mostra(self) -> None:
        print(f'Conteggio attuale: {self.get()}')

        

        
