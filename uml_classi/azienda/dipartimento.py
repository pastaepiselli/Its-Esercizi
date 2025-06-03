from uml_classi.azienda.mytipes import *
from citta import *
class Dipartimento:

    _nome: str # mutabile
    _telefono: set[Telefono] # mutabile [1..*] quindi noto alla nascita
    _indirizzo: Indirizzo # certamente noto alla nascita ma [0..1] quindi rimuovibile
    _citta: Citta

    def __init__(self, nome: str, telefono: Telefono, indirizzo: Indirizzo, citta: Citta) -> None:

        self._telefono = set()


        self.set_nome(nome) 
        self.add_telefono(telefono)
        self.set_indirizzo(indirizzo)
        self.set_citta()

    def nome(self) -> str:

        return self._nome
    
    def set_nome(self, new_name: str) -> None:

        self._nome = new_name

    def citta(self) -> Citta:

        return self._citta
    
    def set_citta(self, c: Citta) -> None:

        self._citta = c

    def telefono(self) -> frozenset[Telefono]:
        # in questo caso restituisco una copia non modificabile, e come ottenere una fotografia
        return frozenset(self._telefono)
    
    def add_telefono(self, new_telefono: Telefono) -> None:

        self._telefono.add(new_telefono)

    
    def remove_telefono(self, t: Telefono) -> None:

        if len(self.telefono()) == 1:
            raise RuntimeError('Il dipartimento deve avere almeno un numero di telefono')
        
        elif t not in  self.telefono():
            raise KeyError(f'Non posso rimuovere il numero di telefono {t}, non e presente nei numeri del dipartimento')

    def indirizzo(self) -> Indirizzo:

        return self._indirizzo
    
    def set_indirizzo(self, new_indirizzo: Indirizzo | None) -> None:

        self._indirizzo = new_indirizzo

    def remove_indirizzo(self) -> None:

        self.set_indirizzo(None)

    def __repr__(self):
        
        return f'Dipartimento({self.nome(), self.indirizzo(), *self.telefono()})'
    
    def __str__(self):
        
        if self.indirizzo():
             
            ind_str: str = 'Con sede in ' + str({self.indirizzo})

        else:

            ind_str : str = 'Senza sede'

        tell_str: str = '[' + ', '.join(self.telefono()) + ']'
        return ind_str