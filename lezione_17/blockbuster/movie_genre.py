from film import Film

class Azione(Film):

	__genere: str
	__penale: float

	def __init__(self, id: int, titolo: str) -> None:
		super().__init__(id, titolo)
		self.__genere = 'Azione'
		self.__penale = 3.00

	def getGenere(self) -> str:
		return self.__genere

	def getPenale(self) -> float:
		return self.__penale

	def calcolaPenaleRitardo(self, giorniRitardo: int) -> float:
		penale_totale = self.__penale * giorniRitardo
		return penale_totale

class Commedia(Film):

	__genere: str
	__penale: float

	def __init__(self, id: int, titolo: str) -> None:
		super().__init__(id, titolo)
		self.__genere = 'Commedia'
		self.__penale = 2.50

	def getGenere(self) -> str:
		return self.__genere

	def getPenale(self) -> float:
		return self.__penale

	def calcolaPenaleRitardo(self, giorniRitardo: int) -> float:
		penale_totale = self.__penale * giorniRitardo
		return penale_totale

class Drama(Film):

	__genere: str
	__penale: float

	def __init__(self, id: int, titolo: str) -> None:
		super().__init__(id, titolo)
		self.__genere = 'Drama'
		self.__penale = 2.00

	def getGenere(self) -> str:
		return self.__genere

	def getPenale(self) -> float:
		return self.__penale

	def calcolaPenaleRitardo(self, giorniRitardo: int) -> float:
		penale_totale = self.__penale * giorniRitardo
		return penale_totale