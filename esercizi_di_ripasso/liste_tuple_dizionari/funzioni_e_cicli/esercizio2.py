def moltiplicazione_sotto_valore(mylist: list[int], threshold: int) -> int:
    prod: int = 1
    for elem in mylist:

        #controllo se e un intero
        if elem % 1 == 0:

            if elem < threshold:

                prod *= elem


    return prod

lista_con_threshold: list = [2, 4, 6, 8, 2]
print(moltiplicazione_sotto_valore(lista_con_threshold, 5))



def fattoriale(n: int) -> int:

    if n == 1:

        return 1

    else:

        return n * fattoriale(n - 1)


print(fattoriale(5))




