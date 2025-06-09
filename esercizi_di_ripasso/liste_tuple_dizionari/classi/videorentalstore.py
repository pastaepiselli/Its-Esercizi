from Movie import *
from customer import *

class VideoRentalStore:

    def __init__(self, movies: dict[str, Movie], customers: dict[str, Customer]) -> None:

        self.movies = movies
        self.customers = customers


    def add_movie(self, movie_id: str, title: str, director: str) -> None:

        if movie_id in self.movies:
            print(f'Il film con ID {movie_id} esiste gia')

        else:
            self.movies[movie_id] = Movie(movie_id, title, director)

    def register_customer(self, customer_id: str, name: str) -> None:

        if customer_id in self.customers:
            print(f'Il cliente con ID {customer_id} e gia registrato')
        
        else:
            self.customers[customer_id] = Customer(customer_id, name)

    def rent_movie(self, customer_id: str, movie_id: str) -> None:

        if customer_id not in self.customers:
            print(f'Cliente con ID {customer_id} non trovato')
            return 

        if movie_id not in self.movies:
            print(f'Film con ID {movie_id} non trovato')
            return 

        movie = self.movies[movie_id]

        cliente = self.customers[customer_id]
        cliente.rent_movie(movie)

    def return_movie(self, customer_id: str, movie_id: str) -> None:

        if customer_id not in self.customers:
            raise ValueError(f'Cliente con ID {customer_id} non trovato')
        
        if movie_id not in self.movies:
            raise ValueError(f'Film con ID {movie_id} non trovato')

        # prendo dal dizionario l'oggetto Movie e lo salvo in una variabile su cui dopo chiamo il metodo return_movie()
        movie = self.movies[movie_id]
        movie.return_movie()

        # stessa cosa viene effetuata con Customer
        client = self.customers[customer_id]
        client.return_movie(movie)

    def get_rented_movies(self, customer_id: str) -> list[Movie]:

        if customer_id not in self.customers:
            raise ValueError(f'Il cliente con ID {customer_id} non esiste')

        cliente = self.customers[customer_id]
        return cliente.rented_movies


        
        



        