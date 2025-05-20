from lezione_12.esercizi_classi.cinemacongeteset import MovieCatalog

catalog: MovieCatalog = MovieCatalog()


catalog.add_movie('Steven palle', ['Ritorno allo sburo', 'Casper', 'le canne'])
catalog.add_movie('popa',['canne', 'la mia citta', 'canne 2 il ritorno'])

print(catalog.getCatalog())


# aggiungere un altro fiml a steven palle

catalog.add_movie('Steven palle', ['et'])

print(catalog.getCatalog())

catalog.remove_movie('Steven palle', 'et')

print(catalog.get_movies_by_director('Steven palle'))

print(catalog.search_movies_by_title('canne'))
