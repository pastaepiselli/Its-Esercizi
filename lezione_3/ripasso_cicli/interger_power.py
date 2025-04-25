def integerower(base: int, esponente: int):
    power: int = 1
    for e in range(0, esponente):

        power = power * base

    return power

