def rimbalzo() -> None:
    tempo = 0
    altezza = 0.0
    velocita = 100.0
    rimbalzi = 0

    while rimbalzi < 5:
        print(f"Tempo: {tempo} Altezza: {altezza:.1f}")

        altezza += velocita
        velocita -= 96
        tempo += 1

        if altezza < 0:
            print(f"Tempo: {tempo} Rimbalzo!")
            rimbalzi += 1
            altezza *= -0.5
            velocita *= -0.5

print(rimbalzo( ))
       


        

    
    