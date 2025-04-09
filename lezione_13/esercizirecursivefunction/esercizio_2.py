def compundInterest(m: float, t: int): # t = mesi, m = somma di partenza

    if m == 0:

        return 'Non ci sono soldi sul conto bro...'
    
    elif t == 0:

        return m

    else:

        return float(1.005 * compundInterest(m, t - 1))
    

print(compundInterest(0, 3))
    

