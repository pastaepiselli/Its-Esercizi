
# # while con le condizioni di validazione dei valori
# while x <= 0 or 0 not in sequenza_numeri:
#     if x < 0:
#         x = int(input('Inserire in numero x (intero positivo): '))


#     if not x < 0:
#         y = int(input('Inserire numero intero positivo per la lista sequenza numeri: '))
#         sequenza_numeri.append(y)

# print(sequenza_numeri)
# print(sequenza_numeri.count(x))

# soluzione + swag
def chiedi_numero_positivo(mess: str) -> int:
    while True:
    # uso il try except per gestire l'errore che mi da quando forzo int() su input()
        try:
            # mess preso in input per personalizzarlo sia per x che per la lista
            x = int(input(mess))
            # quando viene inserito un intero controllo sia anche positivo
            if x >= 0:
                break
            else:
                print('Il numero deve essere positivo')
  
    # quando non viene inserito un intero
        except ValueError:
            print('ValueError il numero inserito deve essere un intero')

    
    return x

# numero intero positivo
num = chiedi_numero_positivo('Inserire un numero positivo: ')

# inizializzo la lista di interi
sequenza_numeri: list[int] = []
while True:
    # richiamo la funzione
    num_seq = chiedi_numero_positivo('Inserire una sequenza di numeri positivi, 0 per terminare: ')
    
    # se il numero e 0 (possibile) interrompe la sequenza e appedno
    if num_seq == 0:
        sequenza_numeri.append(num_seq)
        break
    sequenza_numeri.append(num_seq)
    
    
    




