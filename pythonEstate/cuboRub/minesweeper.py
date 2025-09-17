import random
import re
class Board:

    def __init__(self, dim, bombs) -> None:
        self.dim = dim
        self.bombs = bombs

        self.board = self.make_new_board()
        # dopo che ho inserito le bombe assegno i valori agli spazi senza
        self.assing_values_to_board()

        self.selected = set() # le coordinate del quadrato selezionato

    def make_new_board(self):

        # creo la board
        board = [[None for _ in range(self.dim)] for _ in range(self.dim)]
        
        # piazzo le bombe
        bombs_planted = 0
        while bombs_planted < self.bombs:
            loc = random.randint(0, self.dim**2 - 1)
            row = loc // self.dim
            col = loc % self.dim

            if board[row][col] == "*": # se gia presente una bomba
                continue

            board[row][col] = "*"
            bombs_planted += 1
            
        return board

    
    def assing_values_to_board(self):
        for r in range(self.dim): # row
            for c in range(self.dim): # col
                if self.board[r][c] == "*": # se e una bomba continuiamo
                    continue 
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):

        num_neighboring_bombs = 0
        for r in range(max(0, row - 1), min(self.dim - 1,(row + 1) + 1)):
            for c in range(max(0, col - 1), min(self.dim - 1,(col + 1) + 1)):
                if r == row and c == col:
                    # posizione originale
                    continue
                if self.board[r][c] == "*":
                    num_neighboring_bombs += 1

        return num_neighboring_bombs

    def dig(self, row, col) -> bool:
        
        self.selected.add((row, col)) # aggiungiamo i valori selezionati alla tupla 

        if self.board[row][col] == "*":
            return False
        elif self.board[row][col] < 0:
            return True

        # self.board[row][col] == 0, non ci sono bombe nelle vicinanze
        for r in range(max(0, row -1), min(self.dim - 1, (row + 1) + 1)):
            for c in range(max(0, col - 1), min(self.dim - 1,(col + 1) + 1)):
                if r == row and c == col:
                    # non ri seleziona la posizione scelta
                    continue
                self.selected.add((r, c))

        return True

    def __str__(self) -> str: # se printi l'oggetto torna quello che restituiamo nella funzione str
        
        visible_board = [[None for _ in range(self.dim)] for _ in range(self.dim)]
        for row in range(self.dim):
            for col in range(self.dim):
                if (row, col) in self.selected: # se e stato selezionato allora e visibile   
                    visible_board[row][col] = str(self.board[col][row]) 
                else:
                    visible_board[row][col] = ' '

        # per renderolo carino ... copia e incollo questo codice provo a commentare
        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep

def play(dim = 10, num = 10):
    
    board = Board(dim, num)
   
    while len(board.selected) < board.dim**2 - num:
        print(board)
        # regex valida per 0,0 o 0, 0 0,      0
        user_input = re.split(',(\\s)*',input('Where would you like to dig? Input as row, col: '))# 0, 3
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim or col < 0 or col >= board.dim:
            print('Invalid location')
            continue

        # se e valida
        safe = board.dig(row, col) # .dig() ritorna un booleano
        if not safe: # safe == false
            # bomba
            break

    if safe: # se usciamo dal while abbiamo vinto
        print('You won!!')
    else:
        print('Game over')

        # printiamo la board scoperta
        board.selected = [[(r,c) for r in range(board.dim)]for c in range(board.dim)]
        print(board)

if __name__ == '__main__': # runna solo quello che ce sotto questo if
    play()
