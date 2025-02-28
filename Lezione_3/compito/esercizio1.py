parola: str = []
while parola != "fine":
    parola = str(input("Inserire parola: "))
    if parola[0] == parola[-1]:
        print("Primo e ultimo carattere uguali!!")