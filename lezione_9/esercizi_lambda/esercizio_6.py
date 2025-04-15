from functools import reduce
nums: list[int] = [2, 3, 4]

prodotto: int = reduce(lambda x, y:  x * y, nums)

print(prodotto)