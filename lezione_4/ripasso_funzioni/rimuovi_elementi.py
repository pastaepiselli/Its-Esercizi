def rimuovi_elementi(lista: list[int], da_rimuovere: dict[int:int]) -> list[int]:
    mylist: list[int] = []
    for elem in lista:

        if elem in da_rimuovere and da_rimuovere[elem] > 0:
            
            da_rimuovere[elem] = da_rimuovere[elem] - 1
            
        else:

            mylist.append(elem)


    return mylist
            