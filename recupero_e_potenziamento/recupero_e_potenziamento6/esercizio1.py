
def recursivePalindrome(parola: str) -> bool:
    # ritorna true perche una parola con 1 carattere e sempre palindromo
    parola = parola.lower().replace(' ', '') # imposto lower per evitare il confronto 
    if len(parola) < 2:
        return True
    
    # nel caso la lettera di inizio sia diversa a quella della fine allora sicuramente non e palindroma
    if parola[0] != parola[-1]: 
        return False 
    
    # nel caso la parola continui la richiamo fino ad arrivare ad un caso in cui nella parola non ci sono piu lettere
    return recursivePalindrome(parola[1:-1]) 

print(recursivePalindrome('E dio lo gnomo mongoloide'))

