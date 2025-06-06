def conversione(mylist: list[tuple]) -> dict:

    mydict: dict = {}

    for key, value in mylist:

        if key in mydict:

            mydict[key] += value

        else:

            mydict[key] = value

    return mydict


roba: list[tuple] = [('a', 1), ('b', 2), ('c', 3), ('a', 2)]

print(conversione(roba))

    