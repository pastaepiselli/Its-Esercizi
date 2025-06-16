from volo import Volo
from compagnia import Compagnia
from typing import Any

class VoloComp:
    # gli oggetti di questa classe rappresentano i link volo comp
    _volo: Volo # ovviamente immutabile e noto alla nascita
    _compagnia: Compagnia # ovviamente immutabile e noto alla nascita

    def __init__(self, volo: Volo, compagnia: Compagnia) -> None:

        self._volo = volo
        self._compagnia = compagnia

    def volo(self) -> Volo:
        return self._volo

    def compagnia(self) -> Compagnia:
        return self._compagnia

    # definisco hash & eq perche non possono esistere 2 link uguali

    def __hash__(self) -> int:
        return hash((self._volo, self._compagnia))

    def __eq__(self, other: Any) -> bool:

        if type(self) != type(other) or hash(self) != hash(other):
            return False
        
        # controllo nel caso siano dello stesso tipo e abbiano hash uguale

        # controllo con "is" 
        # 2 link sono uguali se i 2 componenti del link se sono indentici per entrambi
        return self.volo() is other.volo() and self.compagnia() is other.compagnia()
         

