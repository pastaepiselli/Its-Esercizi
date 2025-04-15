parole: list[str] = ["cane", "gatto", "elefante", "ratto", "orso"] 

only_four_letters: list[str] = list(filter(lambda name: len(name) > 4, parole))

print(only_four_letters)