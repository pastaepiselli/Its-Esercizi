
x: int = int(input("Inserire punto x:  "))


y: int = int(input("Inserire punto y: "))

coordinate: tuple[int, int] = (x, y) # utilizzare se conosciamo i dati

match coordinate:
    case 0, 0:
        print(f"Il punto {coordinate} si trova nell'origine")
    case 0, y:
        print(f"Il punto {coordinate} si trova sull'asse delle x")
    case x, 0:
        print(f"Il punto {coordinate}si trova sull'asse delle y")
    case coordinate if x > 0 and y > 0:
        print(f"Il punto {coordinate} si trova nel primo quadrante")
    case coordinate if x < 0 and y > 0:
        print(f"Il punto {coordinate} si trova nel secondo quadrante")
    case coordinate if x < 0 and y < 0:
        print(f"Il punto {coordinate} si trova nel terzo quadrante")
    case coordinate if x > 0 and y < 0:
        print(f"Il punto {coordinate} si trova nel quarto quadrante") 