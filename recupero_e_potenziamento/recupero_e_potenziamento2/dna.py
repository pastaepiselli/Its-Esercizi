import re

# funzione per controllo validita dna

def isDna(dna: str) -> bool:
    
    # pattern x la regex >:(
    pattern = r'^[catgCATG]+$'

    if re.fullmatch(pattern, dna):
        return True
    
    return False


s1 = "CAGCTGATCGATGCTAGCCTG"

print(isDna(s1)) # true

print(isDna('toshtnsotnstictfacgt')) # false


def sovrapposizione_dna(s1: str, s2: str) -> int:
    if not isDna(s1):
        raise ValueError('Inserire DNA valido')
    
    if not isDna(s2):
        raise ValueError('Inserire DNA valido')
    # itero sulla lunghezza del dna
    for i in range(len(s1)):
        # vado a diminuire la lunghezza del dna fino a trovare la parte che si collega
        if s1[i:] == s2[:i]:

            dna_piu_lungo = i
    return dna_piu_lungo

def stampa_sovrapposizione(s1: str, s2: str, dna_piu_lungo: int) -> None:
    # printo il primo dna
    print(s1)

    # ripeto lo spazio tante volte quanta e la differenza tra len(s1) e la lunghezza del dna ricavato
    print('' * (len(s1) - dna_piu_lungo) + s2)

    # printo la lunghezza del dna ricavato

    print(f'La massima lunghezza di sovrapposizione e {dna_piu_lungo}')
        

# PROVIAMO      

s1= "GGTACCGTGA"
s2= "CGTGAACCTT"

x = sovrapposizione_dna(s1, s2)
stampa_sovrapposizione(s1, s2, x)



            
