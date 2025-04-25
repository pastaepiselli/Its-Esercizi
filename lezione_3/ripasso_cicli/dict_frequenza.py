def frequency_dict(elements: list) -> dict:

    mydict: dict = {}

    for item in elements:

        if item not in mydict:

            mydict[item] = 1
        
        else:

            mydict[item] += 1

    return mydict


