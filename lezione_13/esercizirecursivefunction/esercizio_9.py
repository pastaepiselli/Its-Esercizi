def vowelRemover(stringa: str):
    vocali: list[str] = ['a', 'e', 'i', 'o' , 'u']
    if stringa == '':

        return ''
    
    else:

        if stringa[0] in vocali:

            return stringa[0] - vowelRemover(stringa[1:])
    
        else:

            pass

print(vowelRemover('ciao'))