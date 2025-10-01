def range_sum(n: int) -> int:
    if n <= 0:
        return n 
    somma = 0
    for i in range(n + 1):
        somma += i
        print(somma)
    print(somma)
    return somma

range_sum(3)