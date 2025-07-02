from enum import StrEnum, auto
from typing import Self
import re

class CodiceFiscale(str):
	# Gli oggetti di questa classe *sono* stringhe
	#  che rispettano il formato del codice fiscale

	def __new__(cls, cf: str) -> Self:
		cff: str = cf.upper().strip() # rendo la stringa maiuscola e senza spazi iniziali e finali
		if re.fullmatch(r'^[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]$', cff):
			return super().__new__(cls, cff)
		
		raise ValueError(f"La stringa '{cff}' non è un codice fiscale italiano valido!")

class RealGEZ(float):
	# Tipo di dato specializzato Reale >= 0
	def __new__(cls, v: float|int|str|bool|Self) -> Self:
		n: float = float.__new__(cls, v) # prova a convertire v in un float

		if n >= 0:
			return n

		raise ValueError(f"Il valore {n} è negativo!")

class IntGZ(int):

    def __new__(cls, n: int):

        if n > 0:

            return super().__new__(cls, n)
        
        raise ValueError('Inserire un numero intero maggiore di zero')


class IntGEZ(int):

    def __new__(cls, n: int):

        if n >= 0:

            return super().__new__(cls, n)
        
        raise ValueError('Inserire un numero intero positivo')

class Genere(StrEnum):

    donna = auto()
    uomo = auto()

class Ruolo(StrEnum):

	segretario = auto()
	direttore = auto()
	progettista = auto()
