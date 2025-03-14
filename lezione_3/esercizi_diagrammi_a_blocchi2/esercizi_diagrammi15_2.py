n: int = int(input("Inserire un numero intero: "))
sumP: int = 0
sumD: int = 0
match n:
    case a if n >= 0 and n <= 100:
        for i in range(1, n + 1):
            if i % 2 == 0:
                sumP += i
        print(f"La somma di tutti i numeri pari compresi tra 1 e {n} e {sumP}")
    case b if n <= 0:
        "Errore"
    case _:
        for i in range(1, n + 1):
            if i % 2 != 0:
                sumD += i
        print(f"La somma di tutti i numeri dispari compresi tra 1 e {n} e {sumD} ")