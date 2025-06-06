def separazione_per_segno(mylist: list[int]):

    mydict: dict[list[int]] = {'positivi': [], 'negativi': []}

    for elem in mylist:

        if elem >= 0:

            mydict['positivi'].append(elem)

        else:

            mydict['negativi'].append(elem)

    return mydict

swaglista: list[int] = [1, 3, 4, -5, -2, 0,-34]


print(separazione_per_segno(swaglista))
