from mytipes import *

class Progetto:

    _nome: str
    _budget: RealGEZ

    def __init__(self, nome: str, budget: RealGEZ) -> None:
        
        self.set_nome(nome)
        self.set_budget(budget)

    def get_nome(self) -> str:

        return self._nome
    
    def set_nome(self, new_nome: str) -> None:

        self._nome = new_nome
    
    def get_budget(self) -> RealGEZ:

        return self._budget
        
    def set_budget(self, new_budget: RealGEZ) -> None:

        self._budget = new_budget



        


    




        
        

