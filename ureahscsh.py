from abc import ABC
import time

class PostOggetto(ABC):
    pass

class OggettoNuovo(PostOggetto):    
    pass

class Asta(OggettoNuovo):
    pass    


i: int = 0

while i < 10:
    try:
        caricamento: str = 'Loading'
        print(caricamento + '.')
        time.sleep(1)
    
    except KeyboardInterrupt('ao'):
        print('Non hai pazienza!')
        break
    


