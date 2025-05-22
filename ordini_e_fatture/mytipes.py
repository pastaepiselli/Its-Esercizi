from enum import *
import re
from typing import Self
class Indirizzo:
    # l'underscore indica attributi protetti, possono accedere anche le sottoclassi di indirizzo
    _via: str
    _civico: int

    def __init__(self, via: str, civico: int) -> None:

        self._via = via
        self._civico = civico

    def via(self):

        return self._via
    
    def civico(self):

        return self._civico
    

    def __hash__(self):
        # l'hash si calcola con i campi dell'init
        return hash( (self._via, self._civico) )
    
    def __eq__(self, other) -> bool:

        if  other is None or  not isinstance(other, type(self)) or hash(self) != hash(other):

            return False
        
        return self._via == other._via and self._civico == other._civico
    


class StatoOrdine(StrEnum):

    in_preparazione = auto()
    inviato = auto()
    da_saldare = auto()
    saldato = auto()

class CodiceFiscale():

    def __init__(self, cf):
        
        self.cf = self.cf_validation(cf)

    def cf_validation(self, cf: str) -> str:

        pattern = r'[A-Z]{6}[0-9]{2}[A-Z]{1}[0-9]{2}[A-Z]{1}[0-9]{3}[A-Z]{1}'
        cf = cf.upper()
        if re.match(pattern, cf):

            return cf
        else:

            raise ValueError('Inserire un codice fiscale valido')
        
    def __eq__(self, other) -> bool:
        
        if other is None or \
            not isinstance(other, type(self)) or \
            hash(self) != hash(other):

            return False
        return(self.cf) == (other.cf)
    
    def __hash__(self):
        return hash(self.cf)
    

class PartitaIva(str):

    def __new__(cls, iva: str):

        patten = r'\d{11}'

        if re.match(patten, iva):

            return str.__new__(cls, iva)
        
        else: 

            raise ValueError('DIoni')
        
class Telefono(str):

    def __new__(cls, telefono: str):

        pattern = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
        # pattern migliorato ^\+?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{4,6}$
        if re.match(pattern, telefono):

            return str.__new__(cls, telefono)
        
        else:

            raise ValueError('Inserire un numero di telefono valido')
        
class Email(str):

    def __new__(cls, email: str):

        pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

        if re.match(pattern, email):

            return super().__new__(cls, email)
        
        else:

            raise ValueError('Inserire un email valida')
        

           

        

        
    
            
        

        



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