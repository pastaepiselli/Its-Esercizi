import random


track = ['_' for i in range(70)]




class Tartaruga:
    
    tart = 'T'

    track.append(tart)

    tart_pos = track[0]
   
    def __init__(self):
        self.mossa = 2
        
    
    def movetart(self):
        
        #passo veloce
        if self.mossa >= 1 and self.mossa <= 5:

            tart_pos = track[0 + 3]


            
        #scivolata
        elif self.mossa >= 6 and self.mossa <= 7:
            self.tart_pos =  - self.tart_pos
        #passo lento
        elif self.mossa >= 8 and self.mossa <= 10:
            self.tart_pos + '___' + self.tart_pos

        print(track)


popa = Tartaruga()

i = 0
while i < 10:
    debug = int(input('popa: '))

    popa.movetart()











        


        
        
        

