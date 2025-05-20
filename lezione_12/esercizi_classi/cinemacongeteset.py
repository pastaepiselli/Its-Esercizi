class MovieCatalog:

    def __init__(self):
        self.setCatalog()

    def setCatalog(self) -> None:

        self.catalog: dict[str: list[str]] = {}

    def getCatalog(self) -> dict[str:list[str]]:

        return self.catalog
    
    def add_movie(self, director_name: str, movies: list[str]):
        # check valore valido di director_name
        if not director_name:

            print('Fonrnire un nome valido per il regista')
        # check valore valido di movies
        elif not movies:

            print('Fornire una lista di film valida')
        # se i dati inseriti sono validi
        else:

            # se il regista e presente nel catalogo, aggiungi i file

            if director_name in self.catalog:

                # controlliamo se i film della lista movies siano gia stati inseriti dentro al catalogo
                for movie in movies:

                    if movie in self.catalog[director_name]: # self.catalog[director_name] e la lista dei film del regista director name

                        pass
                        
                    else:

                        self.catalog[director_name].append(movie)
            
            else:

                self.catalog[director_name] = movies

    def remove_movie(self, director_name: str, movie: str) -> None:

        # check valore valido di director_name
        if not director_name:

            print('Fonrnire un nome valido per il regista')
        # check valore valido di movie
        elif not movie:

            print('Fornire un film valido')
        # se i dati inseriti sono validi
        else:

            if director_name in self.catalog:
 
                if movie in self.catalog[director_name]:
                    # rimuovere il film dalla lista
                    self.catalog[director_name].remove(movie)
                # se la lista di film e vuoto
                elif len(self.catalog[director_name]) == 0: # if not self.catalog[director_ name]: indica la stessa cosa

                    remove = input(str('Vuole rimuovere il regista?: S/n'))

                    if remove.lower() == 's':

                        del self.catalog[director_name]
    
    def list_directors(self):

        for registi in self.catalog.keys():

            print(registi)

    def get_movies_by_director(self, director_name: str) -> list[str]:
        
        if not director_name:

            print('Inserier un valore valido per director name')

        else:

            if director_name in self.catalog:

                return self.catalog[director_name]
            
    def search_movies_by_title(self, title: str) -> dict[str:list[str]]:

        new_catalog: dict[str:list[str]] = {}

        for registi, film in self.catalog.items():

            if title in film:

                new_catalog[registi] = 

        return new_catalog


        
    



    




                    



            



            



        
            


