n1 = int(input("Inserire numero A: "))
n2 = int(input("Inserire numero B: "))
if n1 > n2:
    n1, n2 = n2, n1
prodotto: int = 1
for i in range(n1, n2 + 1):
    prodotto = prodotto * i
    
print(f"Il prodotto tra dei numeri tra {n1} e {n2} è {prodotto}")