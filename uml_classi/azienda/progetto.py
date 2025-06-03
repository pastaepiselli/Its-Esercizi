from mytipes import *

class Progetto:

    _nome: str
    _budget: RealGEZ

    def __init__(self, nome: str, budget: RealGEZ) -> None:
        
        self.set_nome(nome)
        self.set_budget(budget)

    def _nome(self) -> str:

        return self._nome
    
    def set_nome(self, new_nome: str) -> None:

        self._nome = new_nome
    
    def budget(self) -> RealGEZ:

        return self._budget
        
    def set_budget(self, new_budget: RealGEZ) -> None:

        self._budget = new_budget

    def __str__(self):
        
        return f'Progetto {self._nome()}, con budget: {self.budget()}$'
    




        


    




        
        

