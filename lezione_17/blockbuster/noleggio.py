from film import Film

class Noleggio():
	def __init__(self, film_list: list[Film]) -> None:
		self.film_list = film_list
		self.rented_film = {}

	def isAvaible(self, film: Film) -> bool:
		if film in self.film_list:
			print(f'Il film scelto e disponibile: {film.getTitle()}!')
			return True
		print(f'Il film scelto non e disponibile: {film.getTitle()}!')
		return False

	def rentMovie(self, film: Film, clientId: int) -> None:
		if self.isAvaible(film):
			self.film_list.remove(film)
			# il cliente gia e registrato come chiave?
			if clientId in self.rented_film:
				# allora aggiungo con append
				self.rented_film[clientId].append(film)
			else:
				# allora creo il dato nel dizionario
				self.rented_film[clientId] = [film]
			print(f'Il cliente {clientId} ha noleggiato il {film.getTitle()}!')
		else:
			print(f'Non e possibile noleggiare il film {film.getTitle()}!')

	def giveBack(self, film: Film, clientId: int, days: int) -> None:
		self.rented_film[clientId].remove(film)
		self.film_list.append(film)
		penale = film.calcolaPenaleRitardo(days)
		print(f'Cliente {clientId}! La penale da pagare per il film {film.getTitle()} e di {penale} euro!')

	def printMovies(self) -> None:
		for film in self.film_list:
			print(f'{film.getTitle()} - {film.getGenere()}')
		
	def printRentMovies(self, clientId: int) -> None:
		print(*self.rented_film[clientId])
