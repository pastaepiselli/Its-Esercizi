from typing import Self, Any

from enum import *


# strEnuem ci per12mette di creare un enumerativo ed usare quei valori come stringhe
class Genere(StrEnum):

    uomo = auto()
    # auto() crea un simbolo con il nome della variabile a cui viene assegnato
    donna = auto()

