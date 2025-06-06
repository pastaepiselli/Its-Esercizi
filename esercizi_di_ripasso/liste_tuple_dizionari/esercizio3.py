def prodotti(mydict: dict[str: int | float]) -> dict[str: int | float]:

    new_dict: dict[str: int | float] = {}

    for key, value in mydict.items():

        perc = (value * 10) / 100
        result = value + perc
        if result < 50:

            new_dict[key] = f'{result:.2f}'

    
    return new_dict


todis: dict =  {'pane': 60, 'pesce': 20, 'pasta': 40, 'raponi': 50}

print(prodotti(todis))

