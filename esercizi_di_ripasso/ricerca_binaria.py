def ricerca_binaria(lista: list[int], search: int) -> bool:
    inizio = 0
    fine = len(lista) - 1

    while inizio <= fine:
        medio = len(lista)  // 2
        if lista[medio] == search:
            return True
        elif lista[medio] < search:
            inizio = medio + 1
        else:
            fine = medio - 1

    return False


def binary_search(lista: list[int], search: int) -> bool:
    
    inizio = 0
    fine = len(lista) - 1
    medio = len(lista) // 2
    print(lista[medio], search)
    if lista[medio] == search:
        return True
        
    elif lista[medio] > search:
        fine = medio - 1
        binary_search(lista[inizio:fine], search)
    else:
        inizio = medio + 1
        binary_search(lista[inizio:fine], search)
        
    

mylist: list[int] = [3, 7, 8, 9, 10, 11, 36, 56]
find = 7

print(binary_search(mylist, find))


        
