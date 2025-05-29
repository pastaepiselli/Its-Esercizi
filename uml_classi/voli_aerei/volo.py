from mytypes import *

from aeroporto import Aeroporto

class Volo:

    _codice: CodiceVolo # mutabile
    _durata_min: IntGEZ  # mutabile
    _aeroportoPartenza: Aeroporto # immutabile
    _aeroportoArrivo: Aeroporto # immutabile ???
    
    

    def __init__(self, codice: CodiceVolo, durata_min: IntGEZ, partenza: Aeroporto, arrivo: Aeroporto ) -> None:
        
        self.set_codice(codice)
        self.set_durata_min(durata_min)

        # controllo che non sia stato inserito lo stesso aeroporto 2 volte
        if partenza.codice() == arrivo.codice():
            raise ValueError(f'L\'aeroporto {partenza} non puo essere sia di partenza che di arrivo')
        
        self._aeroportoPartenza = partenza
        self._aeroportoArrivo = arrivo

        


    def codice(self) -> CodiceVolo:

        return self._codice
    
    def set_codice(self, codice: str) -> None:

        self._codice = codice

    def durata_min(self) -> IntGEZ:

        return self._durata_min
    
    def set_durata_min(self, durata: IntGEZ) -> None:

        self._durata_min = durata

    def aeroportoPartenza(self) -> Aeroporto:

        return self._aeroportoPartenza

    def aeroportoArrivo(self) -> Aeroporto:

        return self._aeroportoArrivo




        


        
