from videorentalstore import VideoRentalStore
from Movie import Movie
from customer import Customer

# Crea lo store vuoto
store = VideoRentalStore({}, {})

# Aggiungi film
store.add_movie("001", "Interstellar", "Christopher Nolan")
store.add_movie("002", "The Matrix", "Wachowski")
store.add_movie("003", "Pulp Fiction", "Quentin Tarantino")

# Aggiungi clienti
store.register_customer("c001", "Marco")
store.register_customer("c002", "Pier")

# Alice noleggia un film
store.rent_movie("c001", "001")  # Interstellar
store.rent_movie("c001", "002")  # The Matrix

# Pier prova a noleggiare lo stesso film
store.rent_movie("c002", "001")  # Interstellar (già noleggiato)

# Mostra film noleggiati da Alice
print("\n Film noleggiati da Marco:")

