def check_each(mylist: list[int]) -> None:
    for num in mylist:
        if num == 5:
            print("Equal")
        elif num > 5:
            print("Bigger")
        else:
            print("Smaller")
        
check_each([5, 5, 7, 8,9, 0])