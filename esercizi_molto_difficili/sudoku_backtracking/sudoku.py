board: list[list[int]] = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
# in input la board, il numero inserito, e la posizione
def valid(board: list[list[int]], num: int, pos: tuple[int, int]) -> bool:

    # check riga
    for i in range(len(board[0])):
        # andiamo a controllare se il numero che abbaiamo inserito e gia stato inserito in quella posizione
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # check colonna
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # check quadrato
    # prendo la posizione dlla colonna e della riga per i quadrati
    quadrato_x = pos[1] // 3
    quadrato_y = pos[0] // 3

    # andiamo a fare un for loop in quel quadrato
    for i in range(quadrato_y * 3, quadrato_y * 3 + 3):  # scorro le righe del quadrato 3x3
        for j in range(quadrato_x * 3, quadrato_x * 3 + 3):  # scorro le colonne del quadrato 3x3
            # controllo se il numero è già presente nel quadrato, escludendo la posizione corrente
            if board[i][j] == num and (i, j) != pos:
                return 

    return True  


def print_board(board: list[list[int]]) -> None:
    for i in range(len(board)):
        # se i e divisibile per 3
        if i % 3 == 0 and i != 0:
            # printo il divisore orizzontale
            print('- - - - - - - - - -')
        # facciamo un ciclo per la lunghezza della prima linea come riferimento (ogni linea e lungua ugualeee)
        for j in range(len(board[i])):
            # printo il separatore verticale, j != 0 per evitare che mi printi la cella anche a sinistra ... 0 % 3 = 0 
            if j % 3 == 0 and j != 0:
            #printo la colonna con end='' per non mandare a capo
                print('|', end='')
                # se siamo all'ultima posizione printiamo il numero ma non mettiamo end='' perche vogliamo andare a capo dopo
            if j == 8:
                # i = in quale lista siamo j = al valore della lista
                print(board[i][j])
            # nel caso siamo in una pozione no lato o no finale
            else:
                """
                per leggibilita andiamo a fare uno spazio (uso operatore piu senno = TypeError: unsupported operand type(s) for +: 'int' and 'str'
                essendo board[i][j] comunque un numero), e usiamo end='' per evitare che vada a capo
                """
            
                print(str(board[i][j]) + ' ', end='')

def find_empty(board: list[list[int]]) -> tuple[int, int] | None:
    # for (la lunghezza delle) le righe (liste) nella lista
    for i in range(len(board)):
        
        # for (la lunghezza della lista dei) valori nelle righe della lista
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # i = righe,  j = colonne

    return None # se non ci sono spazi vuoti

# questa funzione ritorna soltanto se e stata trovata una soluzione
def risolvi(board: list[list[int]]) -> bool:

    vuoti = find_empty(board)
    if not vuoti:
        return True
    else:
        riga = vuoti[0]
        colonna = vuoti[1]
    # ciclo da 1 a 9
    for i in range(1, 10):
        # se il numero e valido 
        if valid(board, i, (riga, colonna)):
            # lo inserisco nella posizione vuota
            board[riga][colonna] = i

            # richiamo la funzione recursivamente (sulla nuova board con il nostro valore inserito) per controllare se ho risolto
            if risolvi(board):
                return True
            
            # poi reimposto il valore a 0
            board[riga][colonna] = 0
    
    # se nessuno di quei numeri e validi allora ritorniamo false
    return False

print_board(board)
risolvi(board)
print('\n')
print_board(board)
