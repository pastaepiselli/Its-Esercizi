def second_since_noon(ore: int, minuti: int, secondi: int) -> int:

    ore = ore * 3600
    minuti = minuti * 60

    resto_secondi: int = ore + minuti + secondi

    return resto_secondi

def time_difference(ore1: int, minuti1: int, secondi1: int, ore2: int, minuti2: int, secondi2: int) -> int:

    if second_since_noon(ore1, minuti1, secondi1) > second_since_noon(ore2, minuti2, secondi2):

        return second_since_noon(ore1, minuti1, secondi1) - second_since_noon(ore2, minuti2, secondi2)
    
    elif second_since_noon(ore2, minuti2, secondi2) > second_since_noon(ore1, minuti1, secondi1):


        return  second_since_noon(ore2, minuti2, secondi2) - second_since_noon(ore1, minuti1, secondi1)
    
    else:

        return 0

