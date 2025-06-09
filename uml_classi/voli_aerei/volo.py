from mytypes import *
from compagnia import *

from aeroporto import Aeroporto

class Volo:

    _codice: CodiceVolo # immutabile
    _durata_min: IntGEZ  # mutabile
    _compagnia: Compagnia

    
    

    def __init__(self, codice: CodiceVolo, durata_min: IntGEZ, compagnia: Compagnia) -> None:
        
        self.set_codice(codice)
        self.set_durata_min(durata_min)
        self._compagnia = compagnia
        # quando aggiungo un volo con una compagnia a quella compagnia viene legato quel volo (aggiunto nel set dei voli della compagnia)
        compagnia.add_volo(self)

        # controllo che non sia stato inserito lo stesso aeroporto 2 volte
        if partenza.codice() == arrivo.codice():
            raise ValueError(f'L\'aeroporto {partenza} non puo essere sia di partenza che di arrivo')
        
        self._aeroportoPartenza = partenza
        self._aeroportoArrivo = arrivo

        


    def codice(self) -> CodiceVolo:

        return self._codice
    

    def durata_min(self) -> IntGEZ:

        return self._durata_min
    
    def set_durata_min(self, durata: IntGEZ) -> None:

        self._durata_min = durata




        


        
