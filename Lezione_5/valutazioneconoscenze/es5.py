def somma_elementi(x: list[int], y: list[int]) -> list[int]:
    
    mylist: list[int] = []
    i: int = 0
    if len(x) != len(y):
        print('Le liste devono essere della stessa lunghezza!')
    else:
        for item in x:
            mylist.append(item + y[i])
        i += 1

    return mylist


