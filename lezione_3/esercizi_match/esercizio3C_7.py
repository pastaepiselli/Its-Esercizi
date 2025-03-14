i: int = 0 
testa: int = 0
croce: int = 0
while i <= 7:
    lancio: str = str(input("Inserire testa o croce: ").lower())
    match lancio:
        case "t":
            testa += 1
        case "c":
            croce += 1
        case _:
            print("E' atterrata di lato")
    i = i + 1

testa_per: float = (testa / 8) * 100

croce_per: float = 100 - testa_per

print(f"Totale 'testa' = {testa}\nPercentuale 'testa' = {testa_per:.2f}%")

print(f"Totale 'croce' = {croce}\nPercentuale 'croce' = {croce_per:.2f}%")




