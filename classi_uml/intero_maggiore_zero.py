from typing import Self

class IntGEZ(int):

    def __new__(cls, v: int | float | Self) -> Self:

        if v < 0:

            raise ValueError(f'Inserire valore v == {v} maggiore di zero')
        return int.__new__(cls, v)