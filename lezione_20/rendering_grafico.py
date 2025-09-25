from abc import ABC, abstractmethod

class Forma(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def getArea(self) -> float:
        pass

    @abstractmethod
    def render(self) -> None:
        pass

class Quadrato(Forma):

    def __init__(self,nome: str, lato: int) -> None:
        super().__init__(nome)
        self.lato = lato

    def getArea(self) -> int:
        return self.lato ** 2

    def render(self) -> None:
        # righe
        print(f'Ecco un {self.name} di lato {self.lato}!')
        for i in range(self.lato):
            for j in range(self.lato):
                if i == 0 or i == self.lato - 1:
                    print('*', end=' ')
                else:
                    if j == 0 or j == self.lato - 1:
                        print('*', end=' ')
                    else:
                        print(' ', end=' ')
            print(' ')

class Rettangolo(Forma):
    def __init__(self, nome: str, base: int, altezza: int) -> None:
        super().__init__(nome)
        self.base = base
        self.altezza = altezza

    def getArea(self) -> int:
        area = (self.base * self.altezza) / 2
        return area

    def render(self) -> None:
        # righe 
        print(f'Ecco un {self.name} avente base {self.base} ed altezza {self.altezza}!')
        for r in range(self.altezza):
            for j in range(self.base):
                if r == 0 or r == self.altezza -1 :
                    print('*', end=' ') 
                else:
                    if j == 0 or j == self.base - 1:
                        print('*', end=' ')
                    else:
                        print(' ', end=' ')
            # va a capo dopo ogni riga
            print(' ')

class Triangolo(Forma):
    def __init__(self, nome, lato: int) -> None:
        super().__init__(nome)
        self.lato = lato
    
    def getArea(self) -> int:
        area = (self.lato * self.lato) / 2
        return area

    def render(self) -> None:
        print(f'Ecco un {self.name} avente base {self.lato} ed altezza {self.name}!')
        for i in range(1, self.lato + 1):
            for j in range(i):
                #lato sx      lato dx       base
                if j == 0 or j == i - 1 or i == self.lato:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
            print('')
        
                  
if __name__ == '__main__':
    quad = Quadrato('Quadrato', 4)
    quad.render()
    print(f'L\'area di questo quadrato vale: {quad.getArea()}')

    rect = Rettangolo('Rettangolo',8, 4)
    rect.render()
    print(f'L\'area di questo rettangolo vale: {rect.getArea()}')

    tri = Triangolo('Triangolo',4)
    tri.render()
    print(f'L\'area di questo triangolo vale: {tri.getArea()}')
