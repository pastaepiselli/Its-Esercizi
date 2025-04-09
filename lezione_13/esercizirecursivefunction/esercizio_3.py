def recursiveFactorial(n: int):

    if n == 1:

        return 1
    
    elif n == 0:

        return 1
    
    else:

        return int(n * recursiveFactorial(n - 1))
    
print(recursiveFactorial(3))