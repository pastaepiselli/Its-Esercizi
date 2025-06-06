class Movie:

        def __init__(movie_id: str, title: str, director: str, is_rented: bool) -> None:


            self.movie_id = movie_id
            self.title = title
            self.director = director
            self.is_rented = is_rented

        def rent(self) -> None:

            if self.is_rented == True:
                print(f'IL film {self.title} e gia noleggiato')

            else:
                self.is_rented == True
        
        def return_movie(self) -> None:

            if self.is_rented == True:
                self.is_rented = False

            else:
                print(f'Il film {self.title} non e stato noleggiato da questo cliente')
                