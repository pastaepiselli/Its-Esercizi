grid: list = ['-', '-', '-',
              '-', '-', '-',
              '-', '-', '-']

playerX: str = "X"
playerY: str = "Y"


# tutte le funzioni che controllano la vittoria ... posso fare un unica funzione se le unisco
def win_horizont(grid, player):

    if grid[0] == grid[1] == grid[2] == player:
        print(f'Vince il il giocatore {player}')

    if grid[3] == grid[4] == grid[5] == player:
        print(f'Vince il il giocatore {player}')

    if grid[6] == grid[7] == grid[8] == player:
        print(f'Vince il il giocatore {player}')

def win_vertical(grid, player):

    if grid[0] == grid[3] == grid[6] == player:
        print(f'Vince il il giocatore {player}')

    if grid[1] == grid[4] == grid[7] == player:
        print(f'Vince il il giocatore {player}')

    if grid[2] == grid[5] == grid[8] == player:
        print(f'Vince il il giocatore {player}')

def win_oblique(grid, player):

    if grid[0] == grid[4] == grid[8] == player:
        print(f'Vince il il giocatore {player}')

    if grid[2] == grid[4] == grid[6] == player:
        print(f'Vince il il giocatore {player}')



def print_grid(grid):

    for elem in grid:
        print(elem)
        # capire come printare la lista in un quadrato


print_grid(grid)



