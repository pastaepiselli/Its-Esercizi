def armonica(n: int):

    if n == 1:

        return 1
    
    elif n <= 0:

        raise ValueError('Inserire numero positivo / diverso da 0')
    
    else:

        return  round(1 / n * armonica(n - 1), 6)


print(armonica(6))