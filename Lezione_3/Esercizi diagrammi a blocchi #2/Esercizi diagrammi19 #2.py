n: int = int(input("Inserire numero: "))

somma: int = 0 
prodotto: int = 0

if n % 2 == 0:
    for i in range(1, n + 1):
        if  i % 4 == 0:
            somma += n
    print(somma)
elif n % 2 != 0:
    for i in range(1, n + 1):
        if i % 2 != 0:
            prodotto *= i 
    print(prodotto)
else:
    print("Errore") 