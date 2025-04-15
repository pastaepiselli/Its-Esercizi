import math
def safe_sqr(n: int):
    n = math.sqrt(n)
    return n

try:
    safe_sqr(-1)

except ValueError:

    print('Inserire un numero positivo!!')


   

    
