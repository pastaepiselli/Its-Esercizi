grid: list = ['-', '-', '-',
              '-', '-', '-',
              '-', '-', '-']

playerX: str = "X"
playerO: str = "O"


# tutte le funzioni che controllano la vittoria ... posso fare un unica funzione se le unisco
def win_horizont(grid, player):

    if grid[0] == grid[1] == grid[2] == player:
        print(f'Vince il il giocatore {player}')
        return True

    if grid[3] == grid[4] == grid[5] == player:
        print(f'Vince il il giocatore {player}')
        return True

    if grid[6] == grid[7] == grid[8] == player:
        print(f'Vince il il giocatore {player}')
        return True

def win_vertical(grid, player):

    if grid[0] == grid[3] == grid[6] == player:
        print(f'Vince il il giocatore {player}')
        return True

    if grid[1] == grid[4] == grid[7] == player:
        print(f'Vince il il giocatore {player}')
        return True

    if grid[2] == grid[5] == grid[8] == player:
        print(f'Vince il il giocatore {player}')
        return True

def win_oblique(grid, player):

    if grid[0] == grid[4] == grid[8] == player:
        print(f'Vince il il giocatore {player}')
        return True

    if grid[2] == grid[4] == grid[6] == player:
        print(f'Vince il il giocatore {player}')
        return True

# che palle 
def check_win(grid, player) -> bool:
    #controllo orizzontale + verticale + obliquo
    if grid[0] == grid[1] == grid[2] == player or\
       grid[3] == grid[4] == grid[5] == player or\
        grid[6] == grid[7] == grid[8] == player or\
       grid[0] == grid[3] == grid[6] == player or\
        grid[1] == grid[4] == grid[7] == player or\
        grid[2] == grid[5] == grid[8] == player or\
        grid[0] == grid[4] == grid[8] == player or\
        grid[2] == grid[4] == grid[6] == player:
        return True
    else:
        return False

def check_tie(grid) -> bool:
    if '-' not in grid:
        return True

    else:
        return False


# ce sicuramente un modo piu elegante per scriverlo ma non mi viene ora...
def print_grid(grid):
    # ITS ICT ACADEMY sto studiando giuro
    row1 = f'{grid[0]} | {grid[1]} | {grid[2]}' 
    row2 = f'{grid[3]} | {grid[4]} | {grid[5]}'
    row3 = f'{grid[6]} | {grid[7]} | {grid[8]}'         

    print(row1)
    print(row2)
    print(row3)



# input player:

def player_move(segno: str) -> None:
    # creo la variabile della scelta a caso tanto devo entrare nel ciclo
    choice = -100
    
    # definisco il ciclo con condizione l'inserimento di un input corretto
    while True:
        # input del numero
        scelta = input('Scegli una casella da 1-9: ')

        # controllo sia realmente stato inserito un numero
        if not scelta.isdigit():
            print('Inserire un numero valido (no stringhe)')
            continue

        # lo forzo ad intero
        scelta = int(scelta)

        # cotrollo numero della casella
        if scelta < 0 or scelta > 9:
            print('Il numero deve essere comperso tra 1-9')
            continue

        if grid[scelta -1] != '-':
            print(f'La casella e gia occupata dal giocatore {grid[scelta - 1]}')
            continue

        grid[scelta - 1] = segno
        break

# manca solo l'algoritmo principale 

def minimax(grid, isMaximizing: bool):
    # controllo se ha vinto il giocatore X
    if check_win(grid, playerX) == True:
        return -1
    
    # controllo se ha vinto il giocatore O
    if check_win(grid, playerO) == True:
        return 1
    
    # se ce un pareggio ritorna 0
    if check_tie(grid) == True:
        return 0
    # il giocatore maximizer e il computer
    if isMaximizing:
        bestScore = -100
        # guardo la griglia e fa una mossa su uno spazio vuoto
        for move in range(0, len(grid)):
            if grid[move] == '-':
                grid[move] = 'O'
                # poi controllo lo stato della partita richiamando la funzione minimax ... isMaximizing e false perche il prossimo turno sara del player
                score = minimax(grid, False)
                # dopo che ha fatto la mossa e ha calcolato il punteggio toglie la mossa
                grid[move] = '-'
                # ridefinisce il bestScore ... nella prima iterazione deve essere sempre ridefinito ecco perch impostiamo -100
                bestScore = max(score, bestScore)

        return bestScore

    # algoritmo per calcolare anche le mosse che puo fare l'altro giocatore ... molto simile mai lui punta a minimizzare il "p"
    else:
        bestScore = +100
        for move in range(0, len(grid)):
            if grid[move]== '-':
                grid[move] = 'X'
                # grid True perche la prox mossa sara del computer
                score = minimax(grid, True)
                grid[move] = '-'
                bestScore = min(score, bestScore)

        return bestScore

def best_move_IA(grid: list, segno: str):   
    best_score = -100
    best_move = None

    for move in range(0, len(grid)):
        if grid[move] == '-':
            grid[move] = segno
            score = minimax(grid, False)
            grid[move] = '-'
        
            if score > best_score:
                best_score = score
                best_move = move

    return best_move

def make_move(move: int, segno: str):
    grid[move] = segno



while True:
    print_grid(grid)
    player_move(playerX)
    if check_win(grid, playerX):
        print("Hai vinto!")
        break
    if check_tie(grid):
        print("Pareggio!")
        break

    move = best_move_IA(grid, playerO)
    make_move(move, playerO)
    if check_win(grid, playerO):
        print_grid(grid)
        print("Hai perso! L'IA ha vinto.")
        break
    if check_tie(grid):
        print("Pareggio!")
        break
    



 