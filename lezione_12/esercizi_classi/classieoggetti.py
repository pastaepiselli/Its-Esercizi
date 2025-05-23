from typing import Self, Any
# con self posso segnare sul def il ritorno di una classe

class Persona:

    nome: str
    cf: str

    def __new__(cls, *args ) -> Self :  # restiruisce un oggetto Persona ... non posso faer -> Persona
        return super().__new__(cls)
    
    def __init__(self, nome: str, cf: str) -> None:

        self.nome = nome
        self.cf = cf

    def __eq__(self, other: Any) -> bool:
        # __eq__ sta a ==

        if not isinstance(other, type(self)): # controllo se un altro oggetto ha la stessa classe
            return False
        return self.cf == other.cf # controlla il nome e ritorna un bool 
    
    # quando facciamo hash di oggetti python ci consiglia di ritornae una tupla con gli attributi
    # con questa funzione possiamo usare gli oggetti in collezioni non hashable... come liste e dizionari

    def __hash__(self) -> int:
        return hash(self.cf)
    
    # senza repr print(oggetto) = <__main__.Persona object at 0x7d81e073a7e0>:
    def __repr__(self):
        return f'Persona {self.cf}'
        # con questa funzione sostituisco quello con il return che scelgo io2
    

alice1: Persona = Persona('Alice', 'AAA')

print(type(alice1))

# mro() lista con tutte le super classi di Persona
print('Superclasse di Persona: ' + str(Persona.mro()))


alessia: Persona = Persona('Alessia', 'AAA')

print(hash(tuple[1, 4]))

# print(hash([2, 5, 6])) # nn e hashable perche essendo qualcosa che cambia cambiera il suo hash

print(hash('popa'))

# 1087599663192564167 hash di 'popa'

print(alice1 is alessia)

bob: Persona = Persona('BOB', 'AAAA')
l: list[Persona] = [bob, alessia, alice1]

print(alice1 in l)

d: dict[Persona: int] = {}


d[alice1] = 27

print(d)


