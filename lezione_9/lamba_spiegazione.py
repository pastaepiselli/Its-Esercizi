# usata per definire una funzione piccola

# lambda argument: expertion

# lambda e una funzione quindi di tipo collable

# from typing import Callable

# Callable[[ArgType, ArgType, ....]], returnType # prima inserisco il tipo degli argomenti poi fuori dalla seconda lista metto il return type


from typing import Callable

multiply: Callable[[int, int], int] = lambda a, b: a * b


# basic lambda

square: Callable[[int], int] = lambda x: x ** 2

print(square(5))

# scriverla come una funzione normale

def square(x: int) -> int:
    return x ** 2

# si usa per migliorare la leggibilita in questo caso con lambda creaimo la funzione su una riga

# esempio 2

moltiplic: Callable[[float, float], float] = lambda a, b: a * b
print(moltiplic(3, 4))

# esempio 3 

positive_or_negative: Callable[[int] , str] = lambda x: 'Positivo' if x > 0 else 'Zero o Negativo'
print(positive_or_negative(5))
print(positive_or_negative(-3))

# esempio 4 
# spesso lambda e utilizzata come argomento di funzioni

# using with filter()

nums: list[int] = [1, 2, 3, 4, 5]

# vogliamo usare filter per prendere dalla lista nums solo i numeri pari

even: list[int] = list(filter(lambda x: x % 2 == 0, nums))

# filter ritorna un oggetto di tipo filter ... uso list per trasformare il risulato il una lista
# filter applica lamba sulla lista nums e quando la condizione e vera x viene aggiunto ad evens


# using with sorted

names: list[str] = ['Alice', 'Bob', 'Charlie']
# vogliamo che questa lista venga ordinata per la lunghezza dei nomi

sorted_by_length: list[str] = sorted(names,key=lambda name: len(name))
print(sorted_by_length)

# sorted prevede (lista su cui agire, key= che permette di usare una lambda per modificare il comportamento di sorted)
# in questo caso lo imposto sulla len(name) quindi la lunghezza dell'elemento
# per ogni elemnto della lista names applica len(name)


# quando usare lambda 

"""
    una funzione che mi serve per un breve periodo di tempo
    non vuoi definire un def
    quando la vai ad inserire in un altra funzione
"""


# utilizzare lambda e regex insieme

import re

words: list[str] = ['abc123', '456' ,'43']


# restituire solo le stringe con solo numeri

only_digits: list[str] = list(filter(lambda x: re.fullmatch(r'\d+' , x), words))
print(only_digits) 


"""
    re.fullmatch(r'\d+', x)  controlla se l'intera stringa sia solo numeri
    lambda: defines this condition inline
    filter(): applies lambda to every string in the list 

"""

