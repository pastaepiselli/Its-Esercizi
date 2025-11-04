import string

def frequency_words(lista: list[str]) -> dict[str,int]:
    d = {}
    for e in lista:
        e = e.lower()
        for p in string.punctuation:
            e = e.replace(p, " ")
        
        e = e.split()
        for w in e:
            d[w] = d.get(w, 0) + 1
    
    return d


a = ['palle, e culo', 'culo, palle, piselli', 'pasta! e piselli?']

b = frequency_words(a)

print(b)
print(string.punctuation)
