def add_one(a: int) -> int:
        add: int = a + 1
        return add

value: int = add_one(17)
print(value)

def add_one_to_list(mylist: list[int]) -> None:
    new_list: list[int] = []
    for num in mylist:
        new_list.append(add_one(num))
    print(new_list)

popa: list[int] = [1, 2, 3]
