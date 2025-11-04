def filtra_e_mappa(prodotti: dict[str:float]) -> dict[str:float]:
    d = {}
    for k,v in prodotti.items():
        if v > 20:
            d[k] = v * 0.9
    return d