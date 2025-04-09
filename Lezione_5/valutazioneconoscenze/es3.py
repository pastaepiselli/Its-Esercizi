def even_odd_pattern(numbers: list[int]) -> list[int]:
    mylist: list[int] = []
    for item in numbers:

        if item % 2 == 0:

            mylist.append(item)
    
    for item in numbers:

        if item not in mylist:

            mylist.append(item)
    

    return mylist