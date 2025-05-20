from datetime import *
class Film:
    
    def __init__(self, titolo: str, durata: tuple[int, int]):
        
        self.titolo = self.check_titolo(titolo)
        self.durata = self.check_durata(durata)

    def check_titolo(self, titolo: str) -> str:

        if not titolo:

            raise ValueError('Il valore titolo non puo essere vuoto')

        else:

            return titolo
        
    def check_durata(self, durata: tuple[int, int]) -> timedelta:

        if not durata:

            raise ValueError('La durata non puo essere un valore vuoto')
        
        elif len(durata) == 2:
            delta: timedelta = timedelta(hours=durata[0], minutes=durata[1])
            return delta
        
    def get_titolo(self) -> str:

        return self.titolo
            


class Sala:


    def __init__(self, numero_identificativo: int, film: Film, posti_totali: int):

        self.numero_identificativo: int = numero_identificativo
        self.film: Film = film
        self.posti_totali: int = posti_totali
        self.posti_prenotati: int = 0

    def __repr__(self):
        
        return f'Sala numero: {self.get_numero_identificativo()}, \nfilm: {self.film.get_titolo()}, posti disponibili: {self.posti_disponibili()}'
    
    def get_film(self):

        return self.film.get_titolo()


    def get_numero_identificativo(self) -> int:

        return self.numero_identificativo
    
    def get_posti_totali(self) -> int:

        return self.posti_totali
    
    def posti_disponibili(self) -> int:

        posti_disp: int = self.get_posti_totali() - self.posti_prenotati
        return posti_disp

    def prenota_posti(self, num_posti: int):
        
        if (self.get_posti_totali() - num_posti) < 0:

            print(f'Non ci sono {num_posti} posti liberi!, posti rimanenti: {self.posti_disponibili()}')

        else:
            self.posti_prenotati += num_posti
            print(f'Posti disponibili, {num_posti} prenotati!')


class Cinema:

    def __init__(self):

        self.sale: list[Sala] = []

    def aggiungi_sala(self, sala: Sala) -> None:

        if not sala:

            raise ValueError('Il parametro sala non puo essere lasciato vuoto')
        
        else:
            
            print('Sala aggiunta correttamente')
            self.sale.append(sala)

    def prenota_film(self, titolo_film: str, num_posti: int) -> None:

        for sale in self.sale:

            if titolo_film == sale.get_film():


                sale.prenota_posti(num_posti)

            else:

                print(f'Il film  {titolo_film} non e ancora nelle nostre sale!')


# creo film

film1: Film = Film('Inception', [1, 30])

# creo cinema

cinema: Cinema = Cinema()


# Aggiunta sale
sala1 = Sala(1, film1, 100)

cinema.aggiungi_sala(sala1)

# prenotazioe

cinema.prenota_film('Inception',80)


    




        











        


