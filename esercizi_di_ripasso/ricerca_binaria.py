def ricerca_binaria(lista: list[int], search: int) -> bool:
    inizio = 0
    fine = len(lista) - 1

    while inizio <= fine:
        medio = (inizio + fine) // 2
        if lista[medio] == search:
            return True
        elif lista[medio] < search:
            inizio = medio + 1
        else:
            fine = medio - 1

    return False
