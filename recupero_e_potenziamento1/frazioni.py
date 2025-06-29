# esercizio 8.A

class Frazione:

    # attributi privati
    _numeratore: int
    _denominatore: int


    def __init__(self, numeratore: int, denominatore: int) -> None:

        self.set_numeratore(numeratore)
        self.set_denominatore(denominatore)


    # metodi get
    def numeratore(self) -> int:
        return self._numeratore

    def denominatore(self) -> int:
        return self._denominatore

    # metodi set
    def set_numeratore(self, numeratore: int) -> None:
        if numeratore % 1 != 0:
            self._numeratore = 13

        else:
            self._numeratore = numeratore

    def set_denominatore(self, denominatore: int) -> None:
        if denominatore % 1 != 0:
            self._denominatore = 5
        
        elif denominatore == 0:
            self._denominatore = 5

        else:
            self._denominatore = denominatore

    def value(self) -> float:
        fraz = self._numeratore / self._denominatore
        return f'{fraz:.3f}'

    def __str__(self) -> str:
        return f'{self._numeratore} / {self._denominatore}'

    # definito per poter printare degli oggetti frazione in una lista
    def __repr__(self) -> str:
        return f'{self._numeratore} / {self._denominatore}'



# esercizio 8.B
def mcd(x: int, y: int) -> int:
    # definisco le liste dei divisori
    div_x: list[int] = []
    div_y: list[int] = []
    # divisore 
    div: int = 1
    while x >= div:
        # divido
        res_div: float = x / div
        # controllo se e un vero divisore
        if res_div.is_integer():
            # aggiungo ai divisori
            div_x.append(div)
        div += 1
    #reimposto il divisore ad 1 
    div: int = 1
    while y >= div:
        # stessa roba
        res_div: float = y / div
        if res_div.is_integer():
            div_y.append(div)
        div += 1
    # converto le 2 liste in set e uso la proprieta dei set di .intersection e ritorno la lista di intersezioni
    popa_intersezione = set(div_x).intersection(set(div_y))
    
    # estraggo il valore piu alto della lista POPA
    return max(popa_intersezione)

# esericizio 8.C

def semplifica(lista_frazioni: list[Frazione]) -> list[Frazione]:
    # creo la lista da ritornare di frazioni semplificate
    fraz_semplificate: list[Frazione] = []

    #itero sulla lista in input
    for fraz in lista_frazioni:
        # uso mcd su fraz: Frazione, tra il numeratore e il denominatore per vedere se sono gia semplificate
        if mcd(fraz.numeratore(), fraz.denominatore()) == 1:
            fraz_semplificate.append(fraz)

        else:
            # altrimenti le semplifico, per comodita e leggibilita le salvo in delle variabili
            n = fraz.numeratore()
            d = fraz.denominatore()

            # itero finche non mi trovo con i 2 numeri che mi ritornano un mcd == 1
            while mcd(n, d) != 1:
                # divido sempre per il mcd finche non rimane 1, ogni volta aggiorno n e d 
                n //= mcd(n, d)
                d //= mcd(n, d)

            # alla fine li imposto
            fraz.set_numeratore(n)
            fraz.set_denominatore(d)

            # e li aggiungo alla lista
            fraz_semplificate.append(fraz)

    return fraz_semplificate

# esercizio 8.D 


def fractionCompare(lista_originale: list[Frazione], lista_semplificata: list[Frazione]) -> None:
    i = 0
    for fraz in lista_originale:
        print(f'Valore frazione originale {fraz.value()} --- Valore frazione semplificata {lista_semplificata[i].value()}')
        i += 1


# esecizio 8.E

# la lista la inizializzo nel if __name__ == "__main__":


if __name__ == "__main__":

    # definisco la classe frazione
    popa: Frazione = Frazione(20, 5)

    # provo le funzioni
    print(popa)
    print(popa.value())

    print(popa.numeratore())
    print(popa.denominatore())

    # e un float quindi il numeratore imposta a 13
    popa.set_numeratore(3.4)
    popa.set_denominatore(9)

    print(popa)
    # esercizio mcd ... ci potrebbe funzionare una frazione ...
    print(mcd(12, 18))
    print(mcd(1, 18))

    #creo le frazioni x la lista ..  popa e la prima frazione
    luca: Frazione = Frazione(6, 4)
    pier: Frazione = Frazione(10, 5)
    l1: list[Frazione] = [luca, pier, popa]
    
    # uso la funzione semplifica sulla lista
    print(semplifica(l1))

    # la assegno ad una variabile per usarla nella funzione fractionCompare()
    l_s1: list[Frazione] = semplifica(l1)
    fractionCompare(l1, l_s1)


    #creo un altra lista di frazioni
    l2: list[Frazione] = [Frazione(2.5, 0), Frazione(1, 2), Frazione(2, 4), Frazione(3, 5), Frazione(6, 9), Frazione(4, 7),\
        Frazione(24, 36), Frazione(12, 36), Frazione(40, 60), Frazione(5, 11),  Frazione(10, 45), Frazione(42, 78), Frazione(9, 15),]

    # uso semplifica per creare un'altra lista di frazioni semplificate
    l_s2: list[Frazione] = semplifica(l2)\
    
    # uso fraction compare per far capire che sono equivalenti
    fractionCompare(l2, l_s2)



        

