voti: int = 0
sum: int = 0
scelta: str = None
while scelta != "no":
    scelta = str(input("Vuole inserire un voto?: ")).lower()
    if scelta == "si":
        voto = int(input("Inserire voto: "))
        if voto > 0:
            voti += 1
            sum += voto
        else:
            print("Inserire un voto valido")
media: int 
if voti > 0:
    media = sum / voti
    print(media)