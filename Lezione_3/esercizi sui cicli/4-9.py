num: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cubes: list = []

for item in num:
    cubi: int = item ** 3
    cubes.append(cubi)
print(cubes)