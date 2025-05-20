import matplotlib.pyplot as plt



# def algoritmo(n: int) -> int:

#     if n % 2 == 0:

#         n /=  2
#         return int(n) 
#     else:

#         n = (3 * n) + 1
#         return n
    

# def congettura_di_collatz(n: int) -> None:
#     if n % 1 != 0:
#         raise ValueError("Inserire numero intero")
#     else:  
#         print(n)
#         while n != 1:
            
#             n = (algoritmo(n))
#             print(n)
            



# congettura_di_collatz(16)

def collatz(n: int):

    numeri: list[float] = [n]

    while n != 1:
        if n % 2 == 0:

            n = n / 2

        else: 

            n = (n * 3) + 1\
            
        numeri.append(n)

    return numeri

numeri: list[float] = collatz(hash('popa'))

# plot e una funzione della libreria matplot che ci consente di creare un grafico
plt.plot(numeri)
# show ce lo fa visualizzare
plt.show()





    