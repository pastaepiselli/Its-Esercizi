name = str(input("Inserire nome: "))
gender = str(input("Inserire gender: ")).lower()

match gender:
    case "m":
        print(f"Nome: {name}")
        print("Gender: Maschio")
    case "f":
        print(f"Nome: {name}")
        print("Gender: Femmina")
    case _:
        print(f"Mi dispiace {name}, non e' possibile procedere con la generazione di un documento di identità!")
        
        
