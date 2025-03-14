parcheggi_max = int(input("Inserire posti massimi: "))

posti_liberi: int = parcheggi_max
opzione: str = ""
while opzione != "esci":
    opzione = str(input("Che vuoi fare amigo (colui che parla è una parcheggiatore abusivo): ")).lower()
    if opzione == "ingresso":
        if posti_liberi > 0:
            posti_liberi -= 1
        else:
            print("Il parcheggio è pieno")
    if opzione == "uscita":
        if posti_liberi < parcheggi_max:
            posti_liberi += 1
        else:
            print("Tutti i parcheggi sono gia libere")
    if opzione == "stato":
        print(f"I posti liberi sono {posti_liberi} e i posti occupati sono {parcheggi_max - posti_liberi}")        
    else:
        print("Amigo non capisco")