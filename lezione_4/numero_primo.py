def prime_number(n: int) -> bool:

    counter: int = 0


    if n < 0:

        raise ValueError('Inserire un numero positivo')
    
    elif n == 0:
        
        return False
    
    else:

        for i in range(1, n + 1):

            if n % i == 0:

                counter += 1

        
        if counter == 2:

            return True
        
        else:

            return False
        

print(prime_number(5333))









