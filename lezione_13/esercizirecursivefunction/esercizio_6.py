def produttoria(n: int):

    if n == 0:

        return 2    
    elif n < 0:

        raise ValueError('Inserire numero positivo')
    else:

        return (n + 2) * produttoria(n - 1)
    
print(produttoria(7))   