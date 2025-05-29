from enum import *
import re
from typing import Self, Any

class Genere(StrEnum):

    donna = auto()
    uomo = auto()

class CAP(str):

    def __new__(cls, cap: str):

        if re.fullmatch(r'^[0-9]{5}$', cap):

            return super().__new__(cls, cap)
        raise ValueError(f'{cap}, non e un CAP italiano valido')


class IntGEZ(int):

    def __new__(cls, n: int):

        if n > 0:

            return super().__new__(cls, n)
        
        raise ValueError('Inserire un numero intero positivo')
class Indirizzo:
    # l'underscore indica attributi protetti, possono accedere anche le sottoclassi di indirizzo
    _via: str
    _civico: int

    def __init__(self, via: str, civico: int, cap: CAP) -> None:

        self._via = via
        self._civico = civico
        self._cap = cap

    def via(self):

        return self._via
    
    def civico(self):

        return self._civico
    
    def cap(self) -> CAP:

        return self._cap
    
    def __repr__(self):
        return f'Indirizzo(via={self._via} {self._civico} cap= {self._cap})'
    

    def __hash__(self):
        # l'hash si calcola con i campi dell'init
        return hash( (self._via, self._civico) )
    
    def __eq__(self, other) -> bool:

        if  other is None or  not isinstance(other, type(self)) or hash(self) != hash(other):

            return False
        
        return self._via == other._via and self._civico == other._civico and self._cap == other._cap
    
class CodiceVolo(str):

    def __new__(cls, codice: str | Self) -> Self:

        if re.fullmatch(r'^[A-Z]{1,2}\d{1,4}$', codice):

            return super().__new__(cls, codice)
        
        raise ValueError(f'Il codice {codice} non e valido')
    

class CodiceAeroporto(str):

    def __new__(cls, codice: str) -> Self:


        if re.fullmatch(r'[A-Z]{3}', codice):

            return super().__new__(cls, codice)
        
        raise ValueError(f'Il codice {codice} non e un codice aeroporto valido')
    

class Int1900(int):

    def __new__(cls, x: int) -> Self:

        if x >= 1900:

            return super().__new__(cls, x)
        
        raise ValueError('L\'anno deve essere superiore al 1900')



class StatoOrdine(StrEnum):

    in_preparazione = auto()
    inviato = auto()
    da_saldare = auto()
    saldato = auto()

# class CodiceFiscale():

#     def __init__(self, cf):
        
#         self.cf = self.cf_validation(cf)

#     def cf_validation(self, cf: str) -> str:

#         pattern = r'[A-Z]{6}[0-9]{2}[A-Z]{1}[0-9]{2}[A-Z]{1}[0-9]{3}[A-Z]{1}'
#         cf = cf.upper().strip()
#         if re.match(pattern, cf):

#             return cf
#         else:

#             raise ValueError('Inserire un codice fiscale valido')
        
#     def __eq__(self, other) -> bool:
        
#         if other is None or \
#             not isinstance(other, type(self)) or \
#             hash(self) != hash(other):

#             return False
#         return(self.cf) == (other.cf)
    
#     def __hash__(self):
#         return hash(self.cf)

# codice fiscale migliorato
class CodiceFiscale(str):

    # gli oggetti di questa *sono* stringhe
    # che rispettano il formato del codice fiscale

    def __new__(cls, cf: str) -> Self:

        cff: str = cf.upper().strip()

        if re.fullmatch(r'[A-Z]{6}[0-9]{2}[A-Z]{1}[0-9]{2}[A-Z]{1}[0-9]{3}[A-Z]{1}', cf):

            return super().__new__(cls, cf)
        
        raise ValueError(f'La stringa {cff} non e un codice fiscale valido')
    

class PartitaIva(str):

    def __new__(cls, iva: str):

        patten = r'\d{11}'

        if re.match(patten, iva):

            return super().__new__(cls, iva)
        raise ValueError('Inserire una partita iva valida')

class Telefono(str):

    def __new__(cls, telefono: str):

        pattern = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
        # pattern migliorato ^\+?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{4,6}$
        if re.match(pattern, telefono):

            return str.__new__(cls, telefono)
        
        else:

            raise ValueError('Inserire un numero di telefono valido')


class RealGEZ(float):

    def __new__(cls, num: int | float):

        if num > 0:

            return super().__new__(cls, num)
        
        raise ValueError(f'Il numero {num} deve essere un numero maggiore di zero')
    
            
class Email(str):

    def __new__(cls, email: str):

        pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

        if re.match(pattern, email):

            return super().__new__(cls, email)
        
        else:

            raise ValueError('Inserire un email valida')
        

class Cap(str):
    
    def __new__(cls, cap: str) -> Self:

        if re.fullmatch(r'^\d{5}', cap):

            return super().__new__(cls, cap)
        
        raise ValueError(f'{cap} non e un CAP italiano valido')
    
class RealeGEZ(float):  
    # Tipo di dato specilizzato reale >= 0 

    def __new__(cls, x = float | int | str | bool):
        n: float = super().__new__(cls, x)
        
        if n >= 0:

            return n
        raise ValueError(f'Il valore {n} e negativo')

    # sub indica il meno
    def __sub__(self, value):
        return super().__sub__(value)  


class Valuta(str):

    def __new__(cls, v: str) -> Self:

        if re.fullmatch(r'^[A-Z]{3}$'):

            return super().__new__(cls, v)
        
        raise ValueError(f'La stringa {v} non e un codice valido per una valuta')
    

class Denaro:

    # Rappresenta  il tipo di dato concettuale composto
    # con i seguenti campi:
    #   - importo: reale
    #   - valuta: Valuta
    
    _importo: float
    _valuta: Valuta


    def __init__(self, imp: float, val: Valuta):
        self._importo = imp
        self._valuta = val

    def importo(self) -> float:

        return self._importo
    
    def valuta(self) -> Valuta:

        return self._valuta
    
    def __str__(self):
        
        return f'{self.importo()} {self.valuta()}'
    
    def __repr__(self):
        
        return f'Denaro: {self.importo()} unita di valuta {self.valuta()}'

    def __hash__(self):
        
        return hash(self.importo(), self.valuta())
    
    def __eq__(self, other: Any):

        if not isinstance(other, type(self)) or \
        hash(self) != hash(other):
            return False
        # nel secondo return inserisco questo controllo peche potrebbe essere che il loro hash sia uguale
        return self.importo() == other.importo() and \
        self.valuta() == other.valuta()
        
        
    def __add__(self,other: Self) -> Self:

        '''
        Somma self ad un'altra istanza di Denaro, ma solo se la valuta e la stessa
        Restituisce una nuova istanza di Denaro

        '''
        if self.valuta() != other.valuta():
            raise ValueError(f'Non posso sommare importi di valute diverse: {self.valuta()} e  {other.valuta()}')
        somma: float = self.importo() + other.importo()
        return Denaro(somma, self.valuta())
    
    
class FloatDenaro(float):

    _valuta: Valuta

    def __new__(cls, imp: float, valuta: Valuta):
        d = super().__new__(cls, imp)
        
        # setta il campo valuta
        d._valuta = valuta
        return d
    
    def importo(self) -> float:
        # real e una proprieta dei float !!! nn ho ben capito che cosa fa
        return self.real
    
    def valuta(self) -> Valuta:

        return self._valuta
    

    
    def __str__(self):
        
        return f'{self.importo()} {self.valuta()}'
    
    def __repr__(self):
        
        return f'Denaro: {self.importo()} unita di valuta {self.valuta()}'

    def __hash__(self):
        
        return hash(self.importo(), self.valuta())
    
    def __eq__(self, other: Any):

        if not isinstance(other, type(self)) or \
        hash(self) != hash(other):
            return False
        # nel secondo return inserisco questo controllo peche potrebbe essere che il loro hash sia uguale
        return self.importo() == other.importo() and \
        self.valuta() == other.valuta()
        

    def __add__(self,other: Self) -> Self:

        '''
        Somma self ad un'altra istanza di Denaro, ma solo se la valuta e la stessa
        Restituisce una nuova istanza di Denaro

        '''
        if self.valuta() != other.valuta():
            raise ValueError(f'Non posso sommare importi di valute diverse: {self.valuta()} e  {other.valuta()}')
        somma: float = self.importo() + other.importo()
        return FloatDenaro(somma, self.valuta())
    
    def __sub__(self, other: Self):
        self + FloatDenaro(-other, other.valuta())



    

class Studente:

    _matricola: int # <<imm>>, noto alla nascita
    _nome: str # noto alla nascita
    _genere: Genere # noto alla nascita
    _telefono: set[Telefono] # noto alla nascita [1..1]
    _email: set[Email] # non noto alla nascita
    

    def matricola(self) -> int:

        return self._matricola
    
    def nome(self) -> str:
        
        return self._nome
    
    def genere(self) -> Genere:

        return self._genere
    
    def telefono(self) -> frozenset[Telefono]:
        # con frozen set posso fare tutte le funzionalita tranne quelle che lo modificano

        return self._telefono
    
    def email(self):

        return self._email
    
    def set_nome(self, n: str) -> None:

        self._nome = n 

    # per gli attributi mutabili si imposta anche il set
    def set_nome(self, n: str) -> None:

        self._nome = n 

    # per gli attributi mutabili e multivalore

    def add_telefono(self, t: Telefono) -> None:

        self._telefono.add(t)

    def remome_telefono(self, t: Telefono) -> None:

        if len(self.telefono()) > 1:

            self._telefono.remove(t)

        raise RuntimeError('Uno studente deve avere minimo un numero')
        
    
    

    

        
        

        

            
        

        



if __name__ == '__main__':


    x = CodiceFiscale('RSSLNZ05E05M501H')

    y = CodiceFiscale('RSSLNZ05E05M501m')

    print(x == y)


    pier = PartitaIva('12345678901')

    popa = PartitaIva('12345678901')

    print(popa == pier)


    tel = Telefono('3319631735')
    print(tel)

   
    try:

        tel_sba = Telefono('abv32424243')

    except Exception:

        print('p')


class Aliquota(float):

    def __new__(cls, aliquota: float):

        if 0 < aliquota <= 1:

            return super().__new__(cls, aliquota)
        
        else:

            raise ValueError('Inserire  un aliquota valida!')
        
