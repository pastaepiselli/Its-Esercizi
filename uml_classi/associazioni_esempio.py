from __future__ import annotations

from typing import Any

class Studente:
    _nome: str
    _esami: dict[Modulo, Esame] # insieme dei link esame, con responsabilita solo studente

    def __init__(self, nome: str) -> None:
        self._nome = nome

    def nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str) -> None:
        self._nome = nome

    def esami(self) -> frozenset[_Esame]:
        return frozenset(self._esami.values())

    def esame(self, modulo: Modulo) -> int:
        return self._esami[modulo]

    def add_esame(self, modulo: Modulo, voto: int) -> None:
        # utilizzo il dizionario per renderlo piu efficiente
        if modulo in self._esami:
            raise KeyError(f'Lo studente {self.nome()} ha gia supreato il modulo {self.modulo()}')
        l: esame = Esame(self, modulo, voto)
        self._esami.add(l)

    def remove_esame(self, modulo: Modulo) -> None:
        if modulo not in self._esami:
            raise KeyError(f'Lo studente {self.nome()} non ha superato il modulo {modulo.codice()}!')

        del self._esami[modulo]

    def remove_link_esame(self, esame: Esame) -> None:
        # deve essere lo studente stesso che cancella il link
        if esame.studente() != self:
            raise ValueError(f'Il link non e relativo a {self.nome()} ma a {esame.studente()}')

        del self._esami[esame.modulo()]

    def media_voti(self) -> float:
        try:
            somma: int = 0 
            for esame in self._esami():
                somma += esame.voto()

            return somma / len(self._esami)
        except ZeroDivisionError:
            raise RuntimeError(f'{self.nome()} non ha superato esami quindi non ha nessuna media!')


    def __repr__(self) -> str:
        return f" {self.nome()}"
    
class Modulo:
    _codice: str
    
    def __init__(self, codice: str) -> None:
        self._codice = codice

    def codice(self) -> str:
        return self._codice

    def set_codice(self, codice:str) -> None:
        self._codice = codice

    deef 



class _Esame:
    _studente: Studente
    _modulo: Modulo
    _voto: int

    def __init__(self, studente: Studente, modulo: Modulo, voto: int) -> None:
        self._studente = studente
        self._modulo = modulo  
        self._voto = voto

    def voto(self) -> int:
        return self._voto

    def modulo(self) -> Modulo:
        return self._modulo

    def studente(self) -> Studente:
        return self._studente

    def __hash__(self) -> int:
        return hash((self._modulo, self._studente))

    def __eq__(self, other: Any) -> bool:
        if type(self) != type(other) or hash(self) != hash(other):
            return False
        return self.studente is other.studente() or self.modulo() is other.modulo()

    def __repr__(self) -> str:

        return f"{self.studente()} prende {self.voto()} a {self.modulo()}"

    