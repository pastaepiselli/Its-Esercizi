def coodrs(x: int, y: int):
    return x, y

popa = coodrs(1, 2)
print(type(popa))


mylist: list[int] = [1, 3, 5]
print(*mylist)