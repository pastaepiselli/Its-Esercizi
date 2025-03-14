voto = int(input("Inserisci il voto di laurea: "))

match voto:
    case voto if voto >= 106 and voto <= 110:
        print("GPA 4.0")
    case voto if voto >= 101 and voto <= 105:
        print("GPA 3.7")
    case voto if voto >= 96 and voto <= 100:
        print("GPA 3.3")
    case voto if voto >= 91 and voto <= 95:
        print("GPA 3.0")
    case voto if voto >= 86 and voto <= 90:
        print("GPA 2.7")
    case voto if voto >= 81 and voto <= 85:
        print("GPA 2.3")
    case voto if voto >= 76 and voto <= 80:
        print("GPA 2.0")
    case voto if voto >= 70 and voto <= 75:
        print("GPA 1.7")
    case voto if voto >= 66 and voto <= 69:
        print("GPA 1.0")
    case _:
        print("Voto non valido")
    
    


