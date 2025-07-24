from abc import *
from string import ascii_lowercase
import math
from string import punctuation
# Si crei una classe astratta chiamata CodificatoreMessaggio che ha un solo metodo astratto codifica(testoInChiaro),
class CodificatoreMessaggio(ABC):
    # che ha un solo metodo astratto codifica(testoInChiaro)
    @abstractmethod
    def codifica(self, testoInChiaro: str) -> str:
        pass

class DecodificatoreMessaggio(ABC):
    @abstractmethod
    def decodifica(self, testoCodificato: str) -> str:
        pass

# Si crei una classe CifratoreAScorrimento che implementa le classi astratte CodificatoreMessaggio e DecodificatoreMessaggio.
class CifratoreAScorrimento(CodificatoreMessaggio, DecodificatoreMessaggio):

    def __init__(self, chiave: int) -> None:
        self.chiave = chiave
        
    def __sposta_carattere(self, c: str) -> str:

        # prendo l'index della lettera in input 
        if c in ascii_lowercase:
            spostamento = (ascii_lowercase.index(c) + self.chiave) % len(ascii_lowercase)

        if c in punctuation:
            spostamento = (punctuation.index(c) + self.chiave) % len(punctuation)

        # ritorno la lettera spostata
        return ascii_lowercase[spostamento]

    def codifica(self, testoInChiaro: str) -> str:

        testo_codificato = ''
        for c in testoInChiaro.lower():
            # nel caso ci sia uno spazio vuoto 
            if c == ' ':
                testo_codificato += ' '
                continue

            testo_codificato += self.__sposta_carattere(c)
            
        return testo_codificato

    def __decodifica_carattere(self, c: str) -> str:

        if c in ascii_lowercase:
            spostamento = (ascii_lowercase.index(c) - self.chiave) %  len(ascii_lowercase)
        
        if c in punctuation:
            spostamento = (punctuation.index(c) - self.chiave) %  len(punctuation)

        return ascii_lowercase[spostamento]

    def decodifica(self, testoCodificato: str) -> str:
        testo_decodificato = ''
        for c in testoCodificato:
            # nel caso ci sia uno spazio vuoto
            if c == ' ':
                testo_decodificato += ' '
                continue
            testo_decodificato += self.__decodifica_carattere(c)

        return testo_decodificato

    def lettura(self, dir: str) -> str:

        with open(dir) as f:
            testo = f.read()

        return testo

    def scrittura(self, dir: str, testo: str) -> str:

        with open(dir, 'w') as f:
            f.write(testo)

        return testo

class CifratoreACombinazione(CodificatoreMessaggio, DecodificatoreMessaggio):

    def __init__(self, n: int) -> None:
        self.n = n

    def __combinazione(self, testo: str) -> str:

        testo_combinato = ''
        # prendo la meta sempre in eccesso prendendo un elemento in piu nella prima meta
        meta = math.ceil(len(testo) / 2)
        prima_meta = testo[:meta]
        seconda_meta = testo[meta:]
        
        # lunghezza della parte piu corta ... nel primo caso non cambia niente nel secondo caso evito index eerro
        for i in range(len(prima_meta)):

            # questa e crazy
            try:
                # aggiungo prima la prima meta poi la secndoa
                testo_combinato += prima_meta[i]
                testo_combinato += seconda_meta[i]

            # se la prima lista e piu lunga e quindi prova a trovare un index out of range nella seconda
            except IndexError:
                # non ce problema passo e stiamo chill
                pass
    
        return testo_combinato

    def codifica(self, testoInChiaro: str) -> str:
        # il testo codificato 
        testo_codificato  = testoInChiaro
        for i in range(self.n):
            testo_codificato = self.__combinazione(testo_codificato)

        return testo_codificato

    def __decodifica_combinazione(self, testo: str) -> str:
        # abcde fghi ...  1 volta afbgc hdie ... 2 volte ahfdbi gec
        # ad alternare ci sono lettere delle 2 parti con index pari quellle della prima parte sempre in ordine
        # con index dispari quelle della seconoda
        testo_scombinato = ''
        prima_meta = ''
        seconda_meta = ''
        for i in range(len(testo)):

            # se l'index della lista e dispari allora fa parte della prima meta
            if i % 2 == 0:
                prima_meta += testo[i]
            
            # sel l'index e parti allora parte della seconda meta
            else:
                seconda_meta += testo[i]
        testo_scombinato = prima_meta + seconda_meta
        return testo_scombinato

    def decodifica(self, testoCodificato: str) -> str:
        testo_decodificato = testoCodificato

        # eseguo la decodifica per n volte viene eseguita la codifica
        for n in range(self.n):

            testo_decodificato = self.__decodifica_combinazione(testo_decodificato)

        return testo_decodificato

    def lettura(self, dir: str) -> str:

        with open(dir) as f:
            testo = f.read()

        return testo

    def scrittura(self, dir: str, testo: str) -> str:

        with open(dir, 'w') as f:
            f.write(testo)

        return testo

if __name__ == '__main__':
    # TEST DEL CIFRATORE A SCORRIMENTO

    # - Inizializzazione: Viene creato un oggetto CifratoreAScorrimento con una chiave di scorrimento di 3.
    cifratorescorrimento = CifratoreAScorrimento(3)

    # - Lettura del testo: Il testo in chiaro viene letto da un file.
    testo_letto = cifratorescorrimento.lettura('lezione_22/test_lettura_scorrimento.txt')

    # - Codifica: Il testo in chiaro viene codificato utilizzando il cifratore a scorrimento.
    testo_codificato = cifratorescorrimento.codifica(testo_letto)

    # - Scrittura del testo codificato: Il testo codificato viene scritto su un file.
    testo_scritto = cifratorescorrimento.scrittura('/home/lorenzo/Its-Esercizi/lezione_22/test_scrittura_scorrimento.txt', testo_codificato)

    # - Stampa del testo codificato: Il testo codificato viene stampato.
    print(testo_scritto)

    # - Decodifica: Il testo codificato viene decodificato
    testo_decodificato = cifratorescorrimento.decodifica(testo_codificato)

    # - Stampa del testo decodificato: Il testo decodificato viene stampato.
    print(testo_decodificato)

    # TEST DEL CIFRATORE A CONBINAZIONE

    # - Inizializzazione: Viene creato un oggetto CifratoreACombinazione con 3 combinazioni.
    cifratorecombinazione = CifratoreACombinazione(3)

    # - Lettura del testo: Il testo in chiaro viene letto da un file.
    testo_letto_combinazione = cifratorecombinazione.lettura('lezione_22/test_lettura_combinazione.txt')

    # - Codifica: Il testo in chiaro viene codificato utilizzando il cifratore a combinazione.
    testo_codificato_combinazione = cifratorecombinazione.codifica(testo_letto_combinazione)

    # - Scrittura del testo codificato: Il testo codificato viene scritto su un file.
    testo_scritto_combinazione = cifratorecombinazione.scrittura('lezione_22/test_scrittura_combinazione.txt', testo_codificato_combinazione)

    # - Stampa del testo codificato: Il testo codificato viene stampato.
    print(testo_codificato_combinazione)

    # - Decodifica: Il testo codificato viene decodificato
    testo_decodificato_combinazione = cifratorecombinazione.decodifica(testo_codificato_combinazione)

    # - Stampa del testo decodificato: Il testo decodificato viene stampato.
    print(testo_decodificato_combinazione)


    




