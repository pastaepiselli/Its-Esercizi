mammiferi: list[str] = ["cane", "gatto", "cavallo", "elefante", "leone", "balena", "delfino"]
rettili: list[str] = ["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli: list[str] = ["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]
pesci: list[str] = ["squalo", "trota", "salmone", "carpa"]

animale: str = str(input("Inserire animale: "))

habitat: str = str(input("Inserire habitat: ")).lower()


match animale.lower():
    case animale if animale in mammiferi:
        print(f"{animale} appartiene alla categoria dei mammiferi!")
        animal_type = "mammiferi"
    case animale if animale in rettili:
        print(f"{animale} appartiene alla categoria dei rettili!")
        animal_type = "rettili"
    case animale if animale in uccelli:
        print(f"{animale} appartiene alla categoria degli uccelli!")
        animal_type = "uccelli"
    case animale if animale in pesci:
        print(f"{animale} appartiene alla categoria dei pesci!")
        animal_type = "pesci"
    case _:
        print(f"Non so dire in quale categoria classificare l'animale {animale}")
        animal_type = "sconosciuto"

myanimal: dict[str, str] = {"Nome": animale ,"Categoria": animal_type, "Habitat": habitat}

match myanimal:
    case  myanimal if myanimal["Categoria"] == "mammiferi":
        match habitat:
            case habitat if habitat == "acqua":
                match animale:
                    case "delfino" | "balena":
                        print(f"Il / la {animale} vive in {habitat}")
                    case _:
                        print(f"Il {animale}, non puo vivere in {habitat}")
            case habitat if habitat == "terra":
                match animale:
                    case "delfino" | "balena":
                        print(f"Non ho mai sentit di un / una {animale} che vive in {habitat}")
                    case _:
                        print(f"Corretto il {animale} vive in {habitat}")
            case _:
                print(f"Non ho mai sentito di un {animale} che vive in  {habitat}")         
    case myanimal if animal_type == "pesci":
        match habitat:
            case "acqua":
                print(f"Corretto il / la {animale} vive in {habitat}")
            case _:
                print(f"Non ho mai sentito di un / una {animale} che vive in {habitat}")
    case myanimal if animal_type == "rettili":
        match habitat:
            case "terra" | "acqua":
                print(f"Si {animale} puo vivere in {habitat}")
            case _:
                print(f"No seccomane {animale} non puo vivere in {habitat}")
    case myanimal if animal_type == "uccelli":
        match habitat:
            case "aria":
                print(f"Si {animale} vive in {habitat}")
            case _: 
                print(f"Non ho mai sentito di {animale} vivere in {habitat}")
    case _:
        print("Errore habitat sconosciuto")
    