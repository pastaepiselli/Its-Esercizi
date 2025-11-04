def ordina_numeri(lista: list[int]) -> list[int]:
    for i in range(0, len(lista)):
        for j in range(0, len(lista) - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

a = [9, 3, 5, 1, 3, 21, 4]
print(ordina_numeri(a))