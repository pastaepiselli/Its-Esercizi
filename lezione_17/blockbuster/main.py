from film import Film
from movie_genre import * 
from noleggio import Noleggio

if __name__ == '__main__':

	# 5 azione
	io_sono_leggenda = Azione(0, 'Io sono leggenda')
	il_cavaliere_oscuro = Azione(1, 'Il cavaliere oscuro')
	inception = Azione(2, 'Inception')
	joker = Azione(3, 'Joker')
	the_prestige = Azione(4, 'The prestige')

	# 4 commedie

	i_laureati = Commedia(5, 'I laureati')
	il_mammone = Commedia(6, 'Il mammone')
	zoolander = Commedia(7, 'Zoolander')
	una_notte_da_leoni = Commedia(8, 'Una notte da leoni')

	# 1 drama

	everest = Drama(9, 'Everest')

	lista_film = [io_sono_leggenda, il_cavaliere_oscuro, inception, joker, the_prestige, i_laureati, il_mammone, zoolander, una_notte_da_leoni, everest]

	popa_noleggio = Noleggio(lista_film)

	print('Quale film vuoi noleggiare?')

	popa_noleggio.rentMovie(joker, 1)
	popa_noleggio.rentMovie(zoolander, 1)

	print('quello che ci interessa')

	if popa_noleggio.isAvaible(zoolander):
		print('acomanni')

	popa_noleggio.rentMovie(zoolander, 2) # un secondo cliente prova a noleggiare un film gia noleggiato

	popa_noleggio.rentMovie(everest, 3)

	popa_noleggio.giveBack(zoolander, 1, 4)

	print('\n')
	print('Film ancora disponibili:	')
	popa_noleggio.printMovies()
	popa_noleggio.rentMovie(inception, 1)
	popa_noleggio.printRentMovies(1)








