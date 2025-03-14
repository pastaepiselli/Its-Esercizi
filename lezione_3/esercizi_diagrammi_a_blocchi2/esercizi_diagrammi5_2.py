n: int = int(input("Inserire numero intero: "))

quad: int = 0

if n > 0 and n % 1 == 0:
    for i in range(1, n + 1):
        quad = quad + i**2
    print(f"La somma dei quadrati e {quad}") 
else:
    print("Errore il numero inserito deve essere posivo ed intero")
