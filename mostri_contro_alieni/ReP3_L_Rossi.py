import random

# riprendo alcuni tipi di dato 
class IntGEZ(int):

    def __new__(cls, n: int):

        if n >= 0:

            return super().__new__(cls, n)
        
        raise ValueError('Inserire un numero intero positivo')

class Creatura:

    _nome: str # attributo privato

    def __init__(self, nome: str):

        self.setNome(nome)

    def nome(self) -> str:
        return self._nome

    # metodo set del nome con controllo di stringa valida 
    def setNome(self, nome: str) -> None:
        if not isinstance(nome, str):
            self._nome = 'Creatura generica'

        else:
            self._nome = nome
        

    def __str__(self) -> str:
        return f'Creatura: {self.nome()}'

class Alieno(Creatura):

    # attributi privati
    _matricola: int
    _munizioni: list[IntGEZ]

    def __init__(self, nome: str) -> None:
        # eredito nome da creaturara
        super().__init__(nome)

        # imposto la matricola e le munizioni
        self._setMatricola()
        self._setMunizioni()

        # check per nome valido alieno 
        if nome != "Robot":
            print("Attenzione! Tutti gli Alieni devono avere il nome \"Robot\" seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!")
            self._nome = f"Robot-{self._matricola}"
        elif nome == "Robot":
            self._nome = f"Robot-{self._matricola}"

    
    def matricola(self) -> int:
        return self._matricola

    def munizioni(self) -> list[IntGEZ]:
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
    _assalto: list[IntGEZ]

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
    
    def setVittoria(self, urlo_vittoria: str) -> None:
        # controllo se la stringa non sia un concatenazione di numeri, l'altro controllo nn ha molto senso perche se nn e un str da errore ...
        if urlo_vittoria.isdigit() or not isinstance(urlo_vittoria, str):
            self._urlo_vittoria = "GRAAAHHH"

        else:
            self.urlo_vittoria = urlo_vittoria
        
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



