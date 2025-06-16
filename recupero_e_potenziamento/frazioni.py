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
    fraz_semplificate: list[Frazione] = []
    for fraz in lista_frazioni:
        if mcd(fraz.numeratore(), fraz.denominatore()) == 1:
            fraz_semplificate.append(fraz)

        else:
            n = fraz.numeratore()
            d = fraz.denominatore()
            while mcd(n, d) != 1:
                n //= mcd(n, d)
                d //= mcd(n, d)

            fraz.set_numeratore(n)
            fraz.set_denominatore(d)
            fraz_semplificate.append(fraz)

    return fraz_semplificate



        

if __name__ == "__main__":

    popa: Frazione = Frazione(20, 5)


    print(popa)
    print(popa.value())

    print(popa.numeratore())
    print(popa.denominatore())

    # e un float quindi il numeratore imposta a 13
    popa.set_numeratore(3.4)
    popa.set_denominatore(9)

    print(popa)
    
    print(mcd(12, 18))
    print(mcd(1, 18))

    luca: Frazione = Frazione(6, 4)
    pier: Frazione = Frazione(10, 5)
    

    l: list[Frazione] = [luca, pier, popa]

    print(semplifica(l))

    lista_semplificata = semplifica(l)

    

    

