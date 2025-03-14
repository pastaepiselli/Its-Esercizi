# sum1: int = 0
# for i in range(1, 11):
#     sum1 = sum1 + i
# print(sum1)

# sum2: int = 0
# for i in range(20, 38):
#     sum2 = sum2 + i
# print(sum2)

# sum3: int = 0
# for i in range(35, 50):
#     sum3 = sum3 + i
# print(sum3)

def nomefunzione(a: int, b: int): # nome funzione + (in cui inserisco le variabili che utiizzo)
    #codice che va eseguito
    result: int = 0
    for i in range(a, b + 1):
        result += i
    return result
