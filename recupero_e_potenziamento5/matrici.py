
"""
1.A Scrivere una funzione genera() che data in input la dimensione dim della matrice genera una matrice quadrata di dimensione dim x dim, 
ovvero una matrice che ha dim righe e dim colonne.
Ogni elemento di questa matrice è un numero random tra 0 e 13. 
Inoltre, in ogni riga, ogni elemento della riga deve essere diverso dal primo elemento della riga stessa.
"""


import random

def genera(dim: int) -> list[list[int]]:
    matrice: list[list[int]] = []
    
    # itero per le row
    for r in range(dim):

        # visto che devo generare numeri diversi sulla row tra 0 e 14 
        # importato random e prendo "dim" elementi da questa lista tutti diversi         
        row: list[int] = random.sample(range(14), dim)
        # li appendo alla matrice
        matrice.append(row)

    return matrice


gege = (genera(4))

"""
1.B Scrivere una funzione printMAT(), che data in input una matrice, 
la stampa in output, in modo tale che ogni elemento della matrice occupi in output 5 caratteri.
"""


def printMAT(matrice: list[list[int]]) -> None:


    for r in range(len(matrice)):

        for c in range(len(matrice[r])):

            print(f"{matrice[r][c]:<5}", end="")

        print("\n")
printMAT(gege)


"""
1.C Scrivere una funzione calcolaCarico(), che dati in input una matrice, un indice riga r ed un indice colonna c,
 calcola e restituisce il carico della matrice k(r,c) per la riga r e la colonna c.  
"""

def calcolaCarico(matrice: list[list[int]], r: int, c: int) ->  int:
    
    # salvo la somma della riga in una variabile
    somma_riga: int = sum(matrice[r])

    # qua la vado prima a creare
    somma_colonna: int = 0
    for i in range(len(matrice)):
        # aggiungo il valore dell'index c presente su ogni row a somma_colonna
        somma_colonna += matrice[i][c]

    return somma_riga - somma_colonna

print(calcolaCarico(gege, 0, 0))


"""
1.D Scrivere una funzione caricoNullo(), 
che data in input una matrice, restituisce una lista di tuple, 
dove ogni tupla rappresenta una coppia di indici (r,c) per cui il carico della matrice è nullo.
Ovvero, dovete trovare tutte le righe r e le colonne c per cui il carico della matrice k(r,c)=0 e memorizzare ogni coppia (tupla) in una lista.
"""

def caricoNullo(mat: list[list[int]]) -> list[tuple[int, int]]:

    nullo: list[tuple[int, int]] = []

    for r in range(len(mat)):

        for c in range(len(mat[r])):
            temp = calcolaCarico(mat, r, c)
            if temp == 0:
                nullo.append((r, c))
    
    return nullo

print(caricoNullo(gege))


"""
1.E Scrivere una funzione caricoMax(), 
che data in input una matrice restituisce una tupla di indici r e c per i quali si ha il carico massimo della matrice. 
Ovvero, dovete trovare la coppia di indice riga r e indice colonna c per cui il carico k(r,c) ha valore massimo. 
Prima di restituire la tupla di indici (r,c) stampare il valore del carico massimo.

"""

def caricoMax(mat: list[list[int]]) -> tuple[int, int]:

    # inizializzo la variabile un numero basso cosi che venga sostituito alla prima iterazione
    maxvalore: int = - 100
    maxvalore_index: tuple[int, int] = tuple()

    for r in range(len(mat)):

        for c in range(len(mat[r])):
            new_valore: int = calcolaCarico(mat, r, c)
            if new_valore > maxvalore:
                maxvalore = new_valore
                maxvalore_index = (r, c)

    
    return maxvalore, maxvalore_index

print(caricoMax(gege))
            

"""
1.F Scrivere una funzione caricoMin(), 
che data in input una matrice restituisce una tupla di indici r e c per i quali si ha il carico minimo della matrice. 
Ovvero, dovete trovare la coppia di indice riga r e indice colonna c per cui il carico k(r,c) ha valore minimo. 
Prima di restituire la tupla di indici (r,c) stampare il valore del carico minimo.
"""

def caricoMin(mat: list[list[int]]) -> tuple[int, int]:

    minvalore: int = 1000
    minvalore_index: tuple[int, int] = tuple()

    for r in range(len(mat)):
        
        for c in range(len(mat[r])):

            new_valore: int = calcolaCarico(mat, r, c)
            if new_valore < minvalore:
                minvalore = new_valore
                minvalore_index = (r, c)

    return minvalore, minvalore_index

print(caricoMin(gege))