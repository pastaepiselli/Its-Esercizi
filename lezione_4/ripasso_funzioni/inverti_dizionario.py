def inverti_mappa(dizionario: dict[str:int]) -> dict[int: str]:
    mydict: dict[int: str] = {}
    for key, value in dizionario.items():

        if value in mydict:

            continue
        else:

            mydict[value] = key

    return mydict