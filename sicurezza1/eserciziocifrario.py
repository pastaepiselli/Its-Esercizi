def cifratore(text: str) -> list[int]:
    frase_cifrata: list[int] = []
    valore_segreto = 57
    for w in text:
        frase_cifrata.append(ord(w) ^ valore_segreto)

    return frase_cifrata

frase = 'Nel mezzo del cammin di nostra vita'

popa = cifratore(frase)

def decifra(frase_cifrata: list[int], valore_segreto: int) -> str:
    frase_decifrata: str = ''

    for elem in frase_cifrata:

        lettera_decript = elem ^ valore_segreto
        frase_decifrata += chr(lettera_decript)

    return frase_decifrata

print('Frase criptata')
print(popa)

print('Frase decriptata')
popa_decript = decifra(popa, 57)
print(popa_decript)


#  soluzione prof 


# soluzione crazy devo capirla
print(reduce(lambda x,y: x+y, map(lambda x : chr(x ^ key), map(lambda c: ord(c) ^ key, list(msg))), ""))

# la map trasforma una lista in un'altra lista consentendo di modificare gli elementi
l =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(map(lambda x: x * 3, l))

# data la lista l intendo sommare tutti gli elementi tra di loro
print(reduce(lambda x,y: x + y, l, 0))

# 