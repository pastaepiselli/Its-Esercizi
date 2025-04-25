def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    fitrdict: dict[str:float] = {}

    for key, value in prodotti.items():

        if value > 20:

            fitrdict[key] = (value * 10) / 100
    
    return fitrdict