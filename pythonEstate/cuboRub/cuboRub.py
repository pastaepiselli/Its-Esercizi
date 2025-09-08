# 3) Scrivi un algoritmo che permette di risolvere il cubo di rubik partendo da una combinazione.

class Cube:

    def __init__(self) -> None:
        self.front = [['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']]
        self.back = [['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']]
        self.top = [['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']]
        self.bottom = [['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']]
        self.left = [['G', 'G', 'G'], ['G', 'W', 'W'], ['W', 'W', 'W']]
