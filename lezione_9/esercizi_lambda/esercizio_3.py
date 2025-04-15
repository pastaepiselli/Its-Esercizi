nums: list[int] = [5, 12, 17, 18, 24, 32]

evens: list[int] = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
