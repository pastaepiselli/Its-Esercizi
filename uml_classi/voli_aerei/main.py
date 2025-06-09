from nazione import *
from citta import *
from compagnia import *
from aeroporto import *
from volo import *


italia: Nazione = Nazione(nome='Italia')

roma: Citta = Citta(nome='Roma', abitanti=373942794)
milano: Citta = Citta(nome="Milano", abitanti=442344242)

wizard_air: Compagnia = Compagnia(nome="Wizard Air", annofondazione=1985, sede=roma)


fco: Aeroporto = Aeroporto(codice=CodiceAeroporto("FCO"), nome="Aeroporto Leonardo da Vinci")

v1: Volo = Volo(codice=CodiceVolo("W46061"), durata_min=IntGEZ(105), compagnia=wizard_air)

