def primes_up_to(n: int) -> list[int]:
    primi = []
    if n < 2:
        return []
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
           primi.append(i)
    return primi
       
            
   