class Media:

    # attributi

    title: str
    reviews: list[int]

    def __init__(self, title: str) -> None:

        self.set_title(title)
        self.reviews = []

    def get_title(self) -> str:
        return self.title

    def set_title(self, title: str) -> None:
        self.title = title

    def aggiungiValutazione(self, voto: int) -> None:

        if voto >= 1 and voto <= 5:
            self.reviews.append(voto)
            return 
        
        raise ValueError('Il voto deve essere un numero compreso tra 1 e 5')
    
    def getMedia(self) -> int:
        if len(self.reviews) == 0:
            return 0
        somma = sum(self.reviews)
        media = somma / len(self.reviews)
        return round(media, 2)
    
    def getRate(self) -> str:

        match self.getMedia():

            case 1:
                return 'Terribile'
            case 2:
                return 'Brutto'
            case 3:
                return 'Normale'
            case 4:
                return 'Bello'
            case 5:
                return 'Grandioso'
    def ratePercentage(self, voto: int) -> float:

        voti = self.reviews.count(voto)

        percentuale = (voti / len(self.reviews)) * 100
        return percentuale
    
    def recensione(self) -> str:

        return (
    f'Titolo del film: {self.get_title()}\n'
    f'Voto Medio: {self.getMedia()}\n'
    f'Giudizio: {self.getRate()}\n'
    f'Terribile: {self.ratePercentage(1)}\n'
    f'Brutto: {self.ratePercentage(2)}\n'
    f'Normale: {self.ratePercentage(3)}\n'
    f'Bello: {self.ratePercentage(4)}\n'
    f'Grandioso: {self.ratePercentage(5)}'
)



class Film(Media):

    def __init__(self, title: str) -> None:
        super().__init__(title)
        

if __name__ == "__main__":
    # prova di utilizzo

    film1 = Film("Inception")

    film1.aggiungiValutazione(5)
    film1.aggiungiValutazione(4)
    film1.aggiungiValutazione(3)
    film1.aggiungiValutazione(5)
    film1.aggiungiValutazione(2)

    print(film1.recensione())





    

    