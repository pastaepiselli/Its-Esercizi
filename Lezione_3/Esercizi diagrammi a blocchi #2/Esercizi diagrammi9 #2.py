n: int = int(input("Inserire un numero intero positivo: "))

cont_div: int = 0

if n > 0 and n % 1 == 0:
    for i in range(1, 11):
        pops: int = int(input("Inserire 10 numeri: "))
        if pops % n == 0:
            cont_div += 1 
    print(f"I numeri divisibli per {n} sono {cont_div}")   
