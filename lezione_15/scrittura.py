with open('exemple.txt', mode='w', encoding='utf-8') as file:
    message: str = 'Palle cutolo'
    written_char: int = file.write(message)
    print(f'Written characters: {written_char}')


import time
class StopWatch:

    def __init__(self):

        self.start_time = None
        self.end_time = None

    
    def __enter__(self):
        # salva il tempo corrente

        self.start_time = time.time()

        return self
    
    def __exit__(self, exc_type, exc_value, traceback):

        self.end_time = time.time()

        elapsed_time = self.end_time - self.start_time
        print(f'Elapsed time: {elapsed_time:.8f}')

        # le tre varabili exc_type, exc_value, traceback servono il caso di errore per controllare il tipo
        if exc_type is not None:

            print(f'Exception type: {exc_type}')
            print(f'An error occurred: {exc_value}')
            print(f'Traceback: {traceback}')

        # se mettiamo false l'eccezione viene ritornata al chiamante
        return False
        # se invece ritorniamo true l'index error rimane nella funzione (non chrasha e non viene comunicato)


pass 

with StopWatch():

    lista: list[int] = [1,2, 3]

    print('Inizio del programma')
    lista[3]
    print('Fine del programma')




    
    
   