import time
class Timer:

    def __init__(self):

        self.start_time = 0
        self.end_time = 0

    def __enter__(self) -> float:

        self.start_time = time.time()
        return self.start_time
    

    def __exit__(self, exc_type, exc_value, traceback) -> bool  :

        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f'Il tempo impiegato e stato di {elapsed_time:.8f}')

        if exc_type is not None:

            print(f'Exception type: {exc_type}')
            print(f'An error occurred: {exc_value}')
            print(f'Traceback: {traceback}')

        return False

from lezione_4 import bubble_sort 


with Timer():
    l: list[int] = [6, 2, 4, 7, 5, 1, 9, 3, 15, 22]
    bubble_sort(l)

    
     




        