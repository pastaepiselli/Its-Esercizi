def sum_multiples(limit: int) -> int:
    somma = 0
    if limit <= 0:
        return 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            somma += i
    return somma
            
            
        
    