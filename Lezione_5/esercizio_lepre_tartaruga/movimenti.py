import random
def movetart(tart_pos):

    # genero numero casuale da 1 a 10

    movement = random.randint(1, 10)

    match movement:
        
        #passo veloce
        case 1 | 2 | 3 | 4 | 5:
            # ogni volta che aggiungo dei movimenti controllo se siano 70 o se lo superino cosi da evitare indexing error
            if tart_pos + 3 >= 70:
                # quando supeerano o sono uguali ritorno 70 
                return 70
            else:
                tart_pos += 3

        
        #scivolata
        case 6 | 7:
            # controllo se puo tornare indietro oppure sfora
            if tart_pos > 6:
               
                tart_pos -= 6
            else:
        
                tart_pos = 0
        
        #passo lento
        case 8 | 9 | 10:

            if tart_pos + 1 >= 70:

                return 70
            else:
                tart_pos += 1

    return tart_pos

def movelepre(lepre_pos):
    # qua la shit e molto semplice
    movement = random.randint(1, 10)

    match movement:
        
        # riposo
        case 1 | 2:

            lepre_pos += 0 

        # grande balzo
        case 3 | 4:

            if lepre_pos + 9 >= 70:
                return 70
            else:
                lepre_pos += 9

        
        # grande scivolata
        case 5:

            lepre_pos -= 12

            if lepre_pos <= 12:

                lepre_pos = 0


        
        # piccolo balzo
        case 6 | 7 | 8:
            
            if lepre_pos + 1 >= 70:

                return 70
            else:
                lepre_pos += 1
        
        # piccola scivolata   
        case 9 | 10:

           lepre_pos -= 2
           if lepre_pos <= 2:
            
            lepre_pos = 0

        
    return lepre_pos

def movetart_rain(tart_pos):

    # genero numero casuale da 1 a 10

    movement = random.randint(1, 10)

    match movement:
        
        #passo veloce
        case 1 | 2 | 3 | 4 | 5:
            # ogni volta che aggiungo dei movimenti controllo se siano 70 o se lo superino cosi da evitare indexing error
            if tart_pos + 3 >= 70:
                # quando supeerano o sono uguali ritorno 70 
                return 70
            else:
                tart_pos += 3

        
        #scivolata
        case 6 | 7:
            # controllo se puo tornare indietro oppure sfora
            if tart_pos > 6:
               
                tart_pos -= 6
            else:
        
                tart_pos = 0
        
        #passo lento
        case 8 | 9 | 10:

            if tart_pos + 1 >= 70:

                return 70
            else:
                tart_pos += 1

    if tart_pos - 2 <= 0:
        return 0
    else: 
        return tart_pos

def movelepre_rain(lepre_pos):
    # qua la shit e molto semplice
    movement = random.randint(1, 10)

    match movement:
        
        # riposo
        case 1 | 2:

            lepre_pos += 0 

        # grande balzo
        case 3 | 4:

            if lepre_pos + 9 >= 70:
                return 70
            else:
                lepre_pos += 9

        
        # grande scivolata
        case 5:

            lepre_pos -= 12

            if lepre_pos <= 12:

                lepre_pos = 0


        
        # piccolo balzo
        case 6 | 7 | 8:
            
            if lepre_pos + 1 >= 70:

                return 70
            else:
                lepre_pos += 1
        
        # piccola scivolata   
        case 9 | 10:

           lepre_pos -= 2
           if lepre_pos <= 2:
            
            lepre_pos = 0

        
    if lepre_pos - 2 <= 0:
        return 0
    else: 
        return lepre_pos