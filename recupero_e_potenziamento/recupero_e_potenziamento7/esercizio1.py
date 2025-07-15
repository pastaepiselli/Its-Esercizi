def baricentro(v: list[int]) -> int | None:
        somma_destra: int = 0
        somma_totale: int = sum(v)
        for i in range(len(v)):
            # sommo il primo eemento alla somma destra
            somma_destra += v[i]

            # ricavo la somma sinistra e controllo
            somma_sinistra: int = somma_totale - somma_destra 
            
            # controllo se le due sono uguali
            if somma_destra == somma_sinistra:
                # se sono uguali ritorno l'indice
                return i

        return None


def printResult(v: list[int]) -> None:
    # se la funzione che ritorna l'indice oppure None ritorna None allora il baricentro non esiste
    if baricentro(v) == None:
        print(f'Il baricentro del vettore v={v} non esiste!')
        return
    
    # nel caso esista un baricentro
    print(f'Esiste il baricentro del vettore v={v} ed e dato dall\'indice i={baricentro(v)}')

# gia era ottimizzato il codice ora faccio proprio quello che dice il codice
def baricentroOttimizzato(v: list[int]) -> int | None:
    somma_totale: int = 0
    for i in range(len(v)):
        somma_totale += v[i]
    
    somma_destra: int = 0
    for i in range(len(v)):
        somma_destra += v[i]

        if somma_destra == somma_totale - somma_destra:
            return i
        
        

    return None




if __name__ == '__main__':
    
    v1 = [1, 2, 3, 2, 5, 2, 1]
    v2 = [2, 0, -1, 4, 6, 3, -1]

    print(baricentro(v1))
    print(baricentro(v2))

    printResult(v1)
    printResult(v2)

    print(baricentroOttimizzato(v1))
    print(baricentroOttimizzato(v2))
