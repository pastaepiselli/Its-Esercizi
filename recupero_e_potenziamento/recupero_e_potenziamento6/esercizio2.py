lista_nomi: list[str] = []
nome: str = ''

# il ciclo si interrompe quando vengono inseriti 30 nomi
while len(lista_nomi) != 30:

    # richiedo un nome in input
    nome = str(input('Inserisci un nome: '))
    
    # nomi con len > 20 o stringhe vuote non sono
    if len(nome) > 20 or not nome:
        print('Il nome non e valido')
        continue
    
    # i nomi devono essere distinti, se inserisco un nome gia presente nella lista il ciclo si interrompe
    if nome in lista_nomi:
        break
    lista_nomi.append(nome)


print(f'Hai inserito {len(lista_nomi)} distinti')
# max ritorna la parola piu grande, controlla con len() la lunghezza ... evito la funzione
parola_piu_lunga = max(lista_nomi, key=len)
# def trova_stringa_piu_lunga(mylist: list[str]) -> str:

#     stringa_piu_lunga = mylist[0]
#     for elem in mylist:
#         if len(elem) > stringa_piu_lunga:
#             stringa_piu_lunga = elem

#     return stringa_piu_lunga

print(f'Il piu lungo e {parola_piu_lunga} con {len(parola_piu_lunga)} caratteri')


