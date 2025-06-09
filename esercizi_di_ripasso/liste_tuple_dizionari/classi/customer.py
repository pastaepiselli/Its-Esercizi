from Movie import *

class Customer:

    def __init__(self, customer_id: str, name: str) -> None:

        self.customer_id = customer_id
        self.name = name
        self.rented_movies: list[Movie] = []

    def rent_movie(self, movie: Movie) -> None:
        if movie.is_rented == True:
            print(f'Il film {movie.title} e gia noleggiato')

        else:
            self.rented_movies.append(movie)
            movie.rent()

    def return_movie(self, movie: Movie) -> None:
        if movie.is_rented == False:
            raise ValueError('Il film non e noleggiato')

        self.rented_movies.remove(movie)
        movie.return_movie()



            

