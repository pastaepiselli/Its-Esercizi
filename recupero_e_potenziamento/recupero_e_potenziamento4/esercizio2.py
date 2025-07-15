new_list: list = []

def printListBackward(mylist: list) -> list:
    
    if len(mylist) == 0:
        return new_list

    else:
        new_list.append(mylist[-1])
        mylist.remove(mylist[-1])
        return printListBackward(mylist)

x = [1, 2, 3]
print(printListBackward(x))

