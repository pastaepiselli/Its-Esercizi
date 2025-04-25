def calcola_stipendio(ore_lavorate: int) -> int:
    stipendio: int = 0
    for ore in range(1, ore_lavorate + 1):

        stipendio += 10

        if ore > 40:
            stipendio += 5
    
    return stipendio
