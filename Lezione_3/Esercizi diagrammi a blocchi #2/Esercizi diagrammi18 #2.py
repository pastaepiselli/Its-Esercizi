numeri: int = int(input("Inserire quantita di numeri da inserire (interi):  "))

somma: int = 0
media: int = somma / numeri

somma_pari: int = 0 
somma_dispari: int = 0

for i in range(1, numeri + 1):
    n: int = int(input("Inserire numeri: "))
    somma = somma + n
    if n % 2 == 0 and n > media:
        somma_pari += n
    else:
        somma_dispari += n

if somma_pari > somma_dispari:
    print(f"La somma pari e di {somma_pari} ed e maggiore di sommma dispari {somma_dispari}")
elif somma_dispari > somma_pari:
    print(f"La somma dispari e di {somma_dispari} ed e maggiore di sommma pari {somma_pari}")
else:
    print(f"Le 2 somme sono uguali con risultato {somma_pari}")
