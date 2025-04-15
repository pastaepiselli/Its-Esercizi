# import re

# text: str = 'My email is marco@gmail.com'

# # il metodo find ritorna una lista di stringhe

# # re.findall ritorna una lista di stringhe
# result: list[str] = re.findall(r'\S+@\S+', text) # matcha una o piu occorrenze di tutti i caratteri seguiti da una chicciola
# print(result)


# # capire se una stringa inizia con una lettera maiuscola

# text: str = 'Rome Paris'
# # re.match controlla i match solo all'inizio della stringa
# result1: list[str] = re.match(r'[A-Z][a-z]+', text)

# print(result1.group())

# # find numbers

# sext: str = '12345'

# result2: list[str] = re.findall(r'\d\d', sext)

# print(result2)
import re

text: str = 'Il codice e 123-ABC'

# con le parentesi posso aggire sui sotto gruppi
# match = re.search(r'(\d+)-([A-Z])+', text)

# if match:

#     print('Intera corrispondeza:', match.group(0)) # group 0 e la base dei gruppi
#     print('Primo gruppo:' , match.group(1)) # primo gruppo
#     print('Secondo gruppo: ', match.group(2)) # secondo gruppo

import re

text: str = 'abcabcabc'


print('Cattura:', re.findall(r'(abc)+', text)) # output ['abc']
# ricorda l'utilizzo di ?:abc
print('Non cattura: ', re.findall(r'(?:abc)+', text))