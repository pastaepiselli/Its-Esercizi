class Movie:
    def __init__(self, movie_id,title, director) -> None:
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = False
    
    def rent(self) -> None:
        if self.is_rented:
            print(f"Il film '{self.title}' è già noleggiato.")
        else:
            self.is_rented = True
            
    def return_movie(self) -> None:
        if self.is_rented:
            self.is_rented = False
        else:
            print("If film '{self.title}' non è stato noleggiato  da questo cliente")
class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.rented_movies = []
    
    def rent_movie(self, movie) -> None:
        if movie.is_rented:
            print(f"Il film '{movie.title}' è già noleggiato.")
        else:
            self.rented_movies.append(movie)
            movie.rent()
    
    def return_movie(self, movie) -> None:
        if movie in self.rented_movies:
            self.rented_movies.remove(movie)
            movie.return_movie()
        else:
            print(f"Il film '{movie.title}' non è stato noleggiato da questo cliente.")
class VideoRentalStore:
    def __init__(self) -> None:
        self.movies = {}
        self.customers = {}
    
    def add_movie(self, movie_id, title, director) -> None:
        if movie_id in self.movies:
            print(f"Il film con ID{movie_id} esiste già.")
        else:
            self.movies[movie_id] = Movie(movie_id, title, director)
    
    def register_customer(self, customer_id, name) -> None:
        if customer_id in self.customers:
            print(f"Il cliente con ID {customer_id} è gia registrato")
        else:
            self.customers[customer_id] = Customer(customer_id, name)
    def rent_movie(self, customer_id, movie_id) -> None:
        if customer_id in self.customers and movie_id in self.movies:
            self.customers[customer_id].rent_movie(self.movies[movie_id])
        else:
            print(f"Cliente o film non trovato.")
    
    def return_movie(self, customer_id, movie_id) -> None:
            if customer_id in self.customers and movie_id in self.movies:
                self.customers[customer_id].return_movie(self.movies[movie_id])
            else:
                print(f"Cliente o film non trovato.")
    def get_rented_movies(self, customer_id) -> list[Movie]:
        if customer_id in self.customers:
            return self.customers[customer_id].rented_movies
        print("Cliente non trovato.")
        return []