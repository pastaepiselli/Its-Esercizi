a: int = int(input("Inserire A:"))
b: int = int(input("Inserire B: "))

sum: int = 0

if a < b and a > 0 and b > 0 and a % 1 == 0 and b % 1 ==0:
    # somma = sum(list(range(a, b+1))) posso anche non usare in ciclo
    for n in range(a, b + 1):
        sum = sum + n
    print(sum)
else:
    print("Inserire numero valido")