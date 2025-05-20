class Prodotto:

    def __init__(self, nome: str, quantita: int):

        self.nome = nome
        self.quantita = quantita

    def __str__(self) -> str:
        
        return f'{self.get_nome()}'

    def get_nome(self) -> str:

        return self.nome
    
    def get_quantita(self) -> int:

        return self.quantita

class Magazzino:

    def __init__(self):


        self.prodotti: list[Prodotto] = []

    def aggiungi_prodotto(self, prodotto: Prodotto) -> None:

        if not prodotto:

            print('Il Prodotto non puo essere un valore vuoto')

        else:

            self.prodotti.append(prodotto)
            print(f'Il prodotto {prodotto.get_nome()} e stato aggiuto correttamente')

    def cerca_prodotto(self, nome: str) -> Prodotto:


        for elem in self.prodotti:

            if nome == elem.get_nome():

                return f'Il prodotto {elem} e in magazzino'
            
    def verifica_disponibilita(self, nome: str) -> str:

        for elem in self.prodotti:

            if nome == elem.get_nome():

                if elem.get_quantita() <= 0:

                    return f'Il prodotto {elem.get_nome()} non ha piu scorte in magazzino'
                
                elif elem.get_quantita() > 0:

                    return f'Il prodotto {elem.get_nome()} e disponibile in quantita {elem.get_quantita()}'
                
            else:

                return f'Il prodotto {nome}, non e presente in magazzino'

                    




                
        
# Creazione prodotti
p1 = Prodotto("Mele", 10)
p2 = Prodotto("Banane", 0)
p3 = Prodotto("Arance", 5)

# Creazione magazzino
mag = Magazzino()

# Aggiunta prodotti
mag.aggiungi_prodotto(p1)
mag.aggiungi_prodotto(p2)
mag.aggiungi_prodotto(p3)

# Ricerca prodotto
mag.cerca_prodotto('Mele')

# Verifica disponibilità
print(mag.verifica_disponibilita("Mele"))
print(mag.verifica_disponibilita("Banane"))
print(mag.verifica_disponibilita("Pere"))  # prodotto non esistente





            
        
        


        
            