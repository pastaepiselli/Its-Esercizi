def charDuplicator(stringa: str):

    
    if len(stringa) == 0:

        return ''
    
    else:

        return stringa[0] * 2 + charDuplicator(stringa[1:])
print(charDuplicator('l'))
