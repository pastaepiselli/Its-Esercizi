i: int = 1 

while i < 12:
    posizione = int(input("Inserire posizione: "))
    if posizione == 0 or posizione > 12:
        print("Inserire posizione valida!")
        continue
    if posizione == 1:
        print(f"Finishing  position: {posizione} \n {posizione}st")
    elif posizione == 2:
        print(f"Finishing  position: {posizione} \n {posizione}nd")
    elif posizione == 3:
        print(f"Finishing  position: {posizione} \n {posizione}rd")
    else:
        print(f"Finishing  position: {posizione} \n {posizione}th")
    i = i + 1
    
