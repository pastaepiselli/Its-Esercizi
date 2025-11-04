def check_combination(conditionA: bool, conditionB: bool, conditionC: bool) -> str:
    # cancella pass e scrivi il tuo codice
    if conditionA or (conditionB and conditionC):
        return "Operazione permessa"
    return "Operazione negata"