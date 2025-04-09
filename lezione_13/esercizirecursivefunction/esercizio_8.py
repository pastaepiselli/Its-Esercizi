def vowelsCounter(string: str):
    vocali: list[str] = ['a', 'e', 'i' , 'o' , 'u']
    if string == '':

        return 0
    
    else:

        if string[0].lower() in vocali:

            return int(1 + vowelsCounter(string[1:]))
        
        else:

            return int(0 + vowelsCounter(string[1:]))
    

print(vowelsCounter('palle'))


