class Polynomial:
    def __init__(self, coeff) -> None:
        self.coeff = coeff
    def evaluate(self, x) -> int:
        somma = 0
        for i in range(len(self.coeff)):
            somma += (self.coeff[i] * x ** i)
        return somma
        
            
    