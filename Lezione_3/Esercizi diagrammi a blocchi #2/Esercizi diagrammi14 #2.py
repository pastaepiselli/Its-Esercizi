from random import randint

punteggio: int = 0

while punteggio != 100:

    d1: int = randint(1, 6)
    d2: int = randint(1, 6)
    print(f"Hai tirato un {d1} e un {d2}")
    rollsum: int = d1 + d2
    if d1 == 6 or d1 == 6 or rollsum == 7:
        punteggio = punteggio  + 10
        print(f"Il tuo punteggio e di {punteggio} punti")
    elif d1 % 2 == 0 and d2 % 2 == 0 and rollsum > 8:
        punteggio = 100
        print(f"Il tuo punteggio e di {punteggio} punti")
    else:
        punteggio = 0
        break

if punteggio == 100:
    print("Hai vinto")
else:
    print("Hai perso")


