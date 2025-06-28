from matrici import *

# richiamando la funzione genera(), genera una matrice di dimensione 5 x 5 e richiamando la funzione printMAT() stampa tale matrice a schermo;

matrice = genera(5)
printMAT(matrice)

# individua quante posizioni sono a carico nullo e quali sono, stampandole a schermo, ricorrendo alla funzione caricoNullo();

print(caricoNullo(matrice))


# stampi a schermo gli indici riga rmax e colonna cmax per cui si ha il carico massimo della matrice. 
# Ricorrendo alla funzione calcolaCarico(), 
# stampare il carico della matrice k(rmax, cmax) per verificare che tale carico sia uguale a quello stampato in output dalla funzione caricoMax();

rmax = caricoMax(matrice)[1][0]
cmax = caricoMax(matrice)[1][1]
print(caricoMax(matrice))

print(rmax)
print(cmax)

print(calcolaCarico(matrice, rmax, cmax))


# stampi a schermo gli indici riga rmin  e colonna cmin per cui si ha il carico minimo della matrice. 
# Ricorrendo alla funzione calcolaCarico(), 
# stampare il carico della matrice k(rmin, cmin) per verificare che tale carico sia uguale a quello stampato in output dalla funzione caricoMin().

rmin = caricoMin(matrice)[1][0]
cmin = caricoMin(matrice)[1][0]

print(caricoMin(matrice))
print(rmin)
print(cmin)

print(calcolaCarico(matrice, rmin, cmin))
