from enum import StrEnum
from typing import Self, Any
import re


class Genere(StrEnum):

    donna = auto()
    uomo = auto()

class Ruolo(StrEnum):

    segretario = auto()
    direttore = auto()
    progettista = auto()


class IntGEZ(int):
    
    def __new__(cls, n: int | Self) -> Self:

        if n >= 0:
            return super().__new__(cls, n)

    raise ValueError('Inserire un numero intero positivo maggiore o uguale a zero')

class RealGEZ(float):

    def __new__(cls, num: int | float) -> Self:

        if num >= 0:
            return super().__new__(cls, num)
        
        raise ValueError(f'Il numero {num} deve essere un numero maggiore o uguale a zero')

class IntGZ(int):

    def __new__(cls, n: int | Self) -> Self:

        if n > 0:
            return super().__new__(cls, n)

    raise ValueError(f'Il numero {n} deve essere maggiore di zero')


class CodiceFiscale(str):
	# Gli oggetti di questa classe *sono* stringhe
	#  che rispettano il formato del codice fiscale

	def __new__(cls, cf: str) -> Self:
		cff: str = cf.upper().strip() # rendo la stringa maiuscola e senza spazi iniziali e finali
		if re.fullmatch(r'^[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]$', cff):
			return super().__new__(cls, cff)
		
		raise ValueError(f"La stringa '{cff}' non è un codice fiscale italiano valido!")