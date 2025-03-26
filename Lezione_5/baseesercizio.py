import random
import time


turtle_pos: int = 0
lepre_pos: int = 0
track = []

for i in range(1, 71):
    track.append('_')


def position(track, turtle_pos, lepre_pos):
    
    if turtle_pos == lepre_pos:
        track[turtle_pos] = 'OUCH'
        print(*track)
        track[turtle_pos] = '_'
    
    else:
        track[turtle_pos] = 'T'
        track[lepre_pos] = 'H'
        print(*track)
        # resetta dopo il movimento
        track[turtle_pos] = '_'
        track[lepre_pos] = '_'

def moveturtle(turtle_pos):
    move_turtle = random.randint(1, 10)
   
    

    if move_turtle >= 1 and move_turtle <= 5: # muove avanti
        turtle_pos += 3
        if turtle_pos > 70:
           turtle_pos = 70

    elif move_turtle >= 5 and move_turtle <= 7:
        turtle_pos -= 6
        
    elif move_turtle >= 8 and move_turtle <= 10:
        turtle_pos += 1
        

    if turtle_pos < 0:
            turtle_pos = 0

    

    return turtle_pos

def movelepre(lepre_pos):
    move_lepre = random.randint(1, 10)

    if lepre_pos > 70:
        lepre_pos = 70

    match move_lepre:
        case 1 | 2:
            lepre_pos += 0
        case 3 | 4:
            lepre_pos += 9
        case 5:
            lepre_pos -= 12
        case 6 | 7 | 8:
            lepre_pos += 1
        case 9 | 10:
            lepre_pos -= 2
    
    if lepre_pos < 0:
        lepre_pos = 0


    return lepre_pos
    


print('BANG!!') 

while turtle_pos < 70 or lepre_pos < 70:


    position(track, turtle_pos, lepre_pos)
    turtle_pos = moveturtle(turtle_pos)
    lepre_pos = movelepre(lepre_pos)
    


    time.sleep(0.1)
