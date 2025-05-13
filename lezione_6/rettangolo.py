from formagenerica import FormaGenerica

class Rettangolo(FormaGenerica):

    def __init__(self):
        super().__init__()

        self.setShape('Rettangolo')

    def draw(self) -> None:
        print(f'\n{self.getShape()}')

        # istruzioni per disegnare un rettangolo 5 x 10


        print('\n', end=' ')
        for i in range(5):

            # inner for

            for j in range(5 * 2):

                # lato a e lato b rettangolo

                if i == 5 - 1 or  i == 0:

                    print('*', end=' ')
                    # con end= il print non va a capo ma continua

                # lato b e lato c rettangolo

                elif j == 0 or j == 5 * 2 - 1:

                    print('*', end=' ')

                # stampare spazio bianco

                else:

                    print(' ', end=' ')
            print('\n', end=' ')