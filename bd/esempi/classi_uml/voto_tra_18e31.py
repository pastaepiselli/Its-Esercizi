from typing import Self

class Voto(int):

    def __new__(cls, v: int | float | Self) -> Self:

        if  v < 18 or  v > 30:

            raise ValueError(f'Il voto v == {v} deve essere tra 18 e 30')
        
        return int.__new__(cls, v)

