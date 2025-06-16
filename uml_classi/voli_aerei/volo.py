from mytypes import *
from compagnia import *

from aeroporto import Aeroporto

class Volo:

    _codice: CodiceVolo # immutabile
    _durata_min: IntGEZ  # immutabile
    _compagnia: Compagnia

    
    

    def __init__(self, codice: CodiceVolo, durata_min: IntGEZ) -> None:
        
        self._codice = codice
        self._durata = durata_min
      
      
    def codice(self) -> CodiceVolo:

        return self._codice
    

    def durata_min(self) -> IntGEZ:

        return self._durata_min




        


        
