def are_anagrams(a: str, b: str) -> bool:
    a = a.lower().replace(' ','')
    b = b.lower().replace(' ','')
    
    return (sorted(a) == sorted(b))