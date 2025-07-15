import random

class Creatura:

    _nome: str # attributo privato

    def __init__(self, nome: str):

        self.setNome(nome)

    def nome(self) -> str:
        return self._nome

    # metodo set del nome con controllo di stringa valida ... valida = NO STRINGA NUMERI, NO VUOTA, SOLO STRINGA ACCETTATA
    def setNome(self, nome: str) -> None:
        if not isinstance(nome, str) or nome == '' or nome.isdigit():
            self._nome = 'Creatura generica'

        else:
            self._nome = nome
        

    def __str__(self) -> str:
        return f'Creatura: {self.nome()}'

class Alieno(Creatura):

    # attributi privati
    _matricola: int
    _munizioni: list[int]

    def __init__(self, nome: str) -> None:
        # eredito nome da creaturara
        super().__init__(nome)

        # imposto la matricola e le munizioni
        self._setMatricola()
        self._setMunizioni()

        # check per nome valido alieno 
        if nome[:6]!= "Robot-":
            print("Attenzione! Tutti gli Alieni devono avere il nome \"Robot\" seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!")
            self._nome = f"Robot-{self._matricola}"
        elif nome == "Robot":
            self._nome = f"Robot-{self._matricola}"

    
    def matricola(self) -> int:
        return self._matricola

    def munizioni(self) -> list[int]:
        return self._munizioni

    def _setMatricola(self) -> None:
        # non prende niente in input e imposta numero random 10000-90000
        self._matricola = random.randint(10000, 90000)

    def _setMunizioni(self) -> None:
        # stessa cosa di set matricola ma qua viene creata una lista di 15 numeri da 0-15 al quadrato
        self._munizioni = [(i**2) for i in range(0, 15)]


    def __str__(self) -> str:
        return f'Alieno: {self.nome()}'


class Mostro(Creatura):

    # definisco attributi privati
    _urlo_vittoria: str
    _gemito_sconfitta: str
    _assalto: list[int]

    def __init__(self, nome: str, urlo_vittoria: str, gemito_sconfitta: str) -> None:
        # eredito il nome ... anche getNome
        super().__init__(nome)
        
        # imposto assalto no input
        self._setAssalto()
        
        # input + controllo
        self.setVittoria(urlo_vittoria)
        self.setSconfitta(gemito_sconfitta)

    def urlo_vittoria(self) -> str:
        return self._urlo_vittoria

    def gemito_sconfitta(self) -> str:
        return self._gemito_sconfitta

    def assalto(self) -> list[int]:
        return self._assalto
    
    def setVittoria(self, urlo_vittoria: str) -> None:
        # controllo se la stringa non sia un concatenazione di numeri, l'altro controllo nn ha molto senso perche se nn e un str da errore ...
        if urlo_vittoria.isdigit() or not isinstance(urlo_vittoria, str):
            self._urlo_vittoria = "GRAAAHHH"

        else:
            self._urlo_vittoria = urlo_vittoria
        
    def setSconfitta(self, gemito_sconfitta: str) -> None:
        # stessa cosa scritta sopra ... 
        if gemito_sconfitta.isdigit() or not isinstance(gemito_sconfitta, str):
            self._gemito_sconfitta = "Uuurghhh"

        else:
            self._gemito_sconfitta = gemito_sconfitta
     
    def _setAssalto(self) -> None:
        # per inizzializzare assalto uso sample che ritorna una lista di n valori presi in un range
        self._assalto = random.sample(range(1, 101), 15)

    def __str__(self) -> str:
        # questo printa il nome con lowercase e uppercase alternate ... prob ce un modo piu efficiente
        nome_mostuoso: str = ""
        upper = False
        for chr in self.nome():
            if upper:
                nome_mostuoso += chr.upper()
                upper = False
            else:
                nome_mostuoso += chr.lower()
                upper = True
        return f'Mostro: {nome_mostuoso}'



def pariUguali(a: list[int], b: list[int]) -> list[int]:
    # # creo la lista di ritornare 
    # c: list[int] = []

    # # inserisco un contatore per ciclare anche sulla seconda lista
    # i: int = 0
    # for elem in a:

    #     # nel caso i numeri solo pari
    #     if elem % 2 == 0 and b[i] % 2 == 0:
    #         c.append(1)

    #     # altrimenti
    #     else:
    #         c.append(0)

    #     # aggirno il contatore per iterare anche sull'altra lista 
    #     i += 1
        
    # return c# creo la lista di ritornare 
    # c: list[int] = []

    # # inserisco un contatore per ciclare anche sulla seconda lista
    # i: int = 0
    # for elem in a:

    #     # nel caso i numeri solo pari
    #     if elem % 2 == 0 and b[i] % 2 == 0:
    #         c.append(1)

    #     # altrimenti
    #     else:
    #         c.append(0)

    #     # aggirno il contatore per iterare anche sull'altra lista 
    #     i += 1
        
    #  soluzioni dioni 
    return [1 if j % 2 == 0 and k % 2 == 0 else 0 for j,k in zip(a, b)]

    
                
def combattimento(a: Alieno, m: Mostro) -> Alieno | Mostro | None:

    # controllo che le classi siano valide ??

    if not isinstance(a, Alieno):
        print('Il combattimento deve avvenire tra un mostro e un alieno!')
        return None

    if not isinstance(m, Mostro):
        print('Il combattimento deve avvenire tra un mostro e un alieno!')
        return None

    # inizio del combattimento

    c = pariUguali(a.munizioni(), m.assalto())

    # la lista ha PIU di 4 elementi 1
    if c.count(1) > 4:
        # vince il mostro
        print(m.urlo_vittoria())
        print(m.urlo_vittoria())
        print(m.urlo_vittoria())
        return m
    
    else:
        # vince l'Alieno
        print(m.gemito_sconfitta())
        print(m.gemito_sconfitta())
        print(m.gemito_sconfitta())
        return a


def proclamaVincitore(c: Creatura) -> None:

    # devo stamapare a schermo un rettangolo

    # altezza
    h = 5

    # larghezza , aggiugo la lunghezza del nome che devo mettere detro il rettangolo
    a = len(c.__str__())
    l = a + 10
    
    # itero su altezza e lunghezza
    for i in range(h):
        for j in range(l):
                # condizioni per cui inserisco * a schermo (bordi)
                if i == 0 or i == (h - 1) or j == 0 or j == (l - 1):
                    print('*', end='')
                
                # appena raggiungo la parte centrale inserisco il nome
                elif i == 2 and j == 5:
                    print(c, end='')
                    # poi gli lascio 5 spazi vuoti con un asterisco finale (con 4 spazi vuoti viene preciso!!)
                    print('     *', end="")

                    # poi interrompo questa iterazione
                    break
                else:
                    print(' ', end='')
        # questo print mi serve dopo ogni riga per andare a capo
        print()

if __name__ == "__main__":
    
    # creo una creatura 
    popa: Creatura = Creatura('Popa')
    print(popa)
    
    # creo un alieno con un nome non conforme
    popasupremo: Alieno = Alieno('Popasupremo') # infatti mi da il messaggio di errore e me lo imposta corretto

    # controllo se viene impostato correttamente
    print(popasupremo)

    # creo un mostro
    popaildistruttore: Mostro = Mostro('popaildistuttore', 'Popaaaaa', '234234')

    # controllo la funzione str
    print(popaildistruttore)
    
    # controllo che funzioni il check di validita per il gemito scofitta 
    print(popaildistruttore.gemito_sconfitta())


    # funzione pari uguali
    print(pariUguali([1, 3, 4, 5, 6, 8, 9], [7, 8, 2 , 5, 6, 8, 9]))


    # inizia il combattimento
    combattimento(popasupremo, popaildistruttore)

    proclamaVincitore(popa)

    # TEST FINALE

    xenomorfo: Alieno = Alieno('Robot')

    archvile: Mostro = Mostro('Archville', 'AAAAAAAALALALAL', 'miaooo...')


    print(xenomorfo)
    print(xenomorfo.munizioni())
    print(archvile)
    print(archvile.assalto())


    print('Combattimento')

    proclamaVincitore(combattimento(xenomorfo, archvile))


    b = Creatura('123')
    print(b)

    prova_alieno: Alieno = Alieno('Robot-3445')
