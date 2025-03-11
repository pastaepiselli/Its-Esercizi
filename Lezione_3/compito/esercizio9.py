# pi: float = 0
# div: int = 1
# termini: int = 0
# segno: int = 1  
# while round(pi, 2) != 3.14:
#     pi += segno * 4 / div
#     segno *= -1
#     div += 2 
#     termini += 1
    
# print(f"Per raggiugere 3.14 sono necessari {termini} termini") 

# pi: float = 0
# div: int = 1
# termini: int = 0
# segno: int = 1  
# while round(pi, 3) != 3.141:      
#     pi += segno * 4 / div
#     segno *= -1
#     div += 2 
#     termini += 1
    
# print(f"Per raggiugere 3.141 sono necessari {termini} termini") 

# pi: float = 0
# div: int = 1
# termini: int = 0
# segno: int = 1  
# while round(pi, 4) != 3.1415:
#     pi += segno * 4 / div
#     segno *= -1
#     div += 2 
#     termini += 1
    
# print(f"Per raggiugere 3.1415 sono necessari {termini} termini")

# pi: float = 0
# div: int = 1
# termini: int = 1
# segno: int = 1  
# while round(pi, 5) != 3.14159:
#     pi += segno * 4 / div
#     segno *= -1
#     div += 2 
#     termini += 1
    
# print(f"Per raggiugere 3.14159 sono necessari {termini} termini") 
 
def serie(target: str = ""):
    pi: float = 0.0 
    segno:int = 1
    denominatore: int = 1
    contatore: int = 0
    
    while True:
        pi+=  segno * (4/ denominatore)


        if str(pi)[:len(target)] == target:
            print(f"Servono {contatore} termini per raggiungere {pi } ")
            
            break

        segno *= -1 

        denominatore += 2

        contatore += 1

(serie("3.141"))