import random
import time
from movimenti import *

tart_pos: int = 0 
lepre_pos: int = 0
track: list = []
tick: int = 0

for i in range(0, 70):
    track.append('_')

def posizioni(track, tart_pos, lepre_pos):
    # u know bro partono dal primo indexing della lista 
    
    if tart_pos == lepre_pos:

        track[tart_pos] = 'OUCH!'
        print(*track) # l'asterisco per formattare senza apici
        # resettare ouch per nn tenerlo nella lista
        track[tart_pos] = '_'

    else:
        # con l'indexing inserisco la t ovvero la posizione 
        track[tart_pos] = 'T'

        # stessa cosa per la lepre
        track[lepre_pos] = 'L'

        # printo le loro posizioni (popa gay)
        print(*track)
 
        # e poi resetto sempre pk senno si salvanoooo
        track[tart_pos] = '_'
        track[lepre_pos] = '_'
        



meteo = 'soleggiato'

print('BANG THEY ARE OFF!!!')
while True:
    
    print(f'Tempo (in secondi): {tick}')
    print(f"Condizioni meteo {meteo}")
    print(f"Popa e alla posizione {tart_pos}, e il pier lions e alla posizione {lepre_pos}")
    
    
    if tart_pos == 70:
        print('Ha vinto la tartaruga Popa!!!')
        break
    elif lepre_pos == 70:
        print('Ha vinto la lepre pier leoni!!!')
        break
    elif tart_pos == 70 and lepre_pos == 70:
        print("ITS A TIE")
        break
    tick += 1
    
    posizioni(track, tart_pos, lepre_pos)

    if (tick % 20) >= 10:
        meteo = 'pioggia' 
        tart_pos  = movetart_rain(tart_pos)
        
        lepre_pos  = movelepre_rain(lepre_pos) 
        
    
    else:
        meteo = 'soleggiato'
        tart_pos = movetart(tart_pos) 
        lepre_pos = movelepre(lepre_pos)   

    time.sleep(0.1)  # vabbe questo contolla la velocita delle iterazioni



            









