n: int = 1 
sumP: int = 0
sumD: int = 0
disp: int = 0
numeri: list[int] = []
conta: int = 0
while n != 0:
    n = int(input("Inserisci un numero (0 per terminare): ")) 
    numeri.append(n)

for num in numeri:
    if num % 2 == 0:
        sumP += num
print(f"La somma dei numeri pari è {sumP}")

for num in numeri:
    if num % 2 != 0:
        disp += 1
        sumD += num
print(f"La media dei numeri dispari è {sumD / disp}")

frequenza_max = max(numeri, key=numeri.count)
conteggio = numeri.count(frequenza_max)
print(f"Numero più frequente: {frequenza_max} ({conteggio} volte)")
