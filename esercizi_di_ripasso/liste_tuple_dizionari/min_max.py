def min_max(lista: list[float]) -> tuple[float, float]:
    minimo = lista[0]
    massimo = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < minimo:
            minimo = lista[i]
        
        if lista[i] > massimo:
            massimo = lista[i]

    return (minimo, massimo)


a = [3, 6, 2, 4, 1, 6, 7, 8, 12]
b = min_max(a)
print(b)