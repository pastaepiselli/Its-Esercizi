def produttoria(n: int):

    if n == 1:

        return 1
    
    elif n <= 0:

        raise ValueError('Inserire numero positivo / diverso da 0')
    
    else:

        return pow(n, 3) * produttoria(n - 1)
    
print(produttoria(5))