class FileManager:

    def __init__(self, path: str, mode: str = 'r', encoding: str = 'utf-8'):

        self.path = path
        self.mode = mode
        self.encoding = encoding
        


    def __enter__(self):
        print('Apertura del file....')
        self.file = open(self.path, mode=self.mode, encoding=self.encoding)

        return self.file

       

    def __exit__(self, exc_type, exc_value, traceback):

        print('Chiusura del file...')
        self.file.close()

        if exc_type is not None:

            print(f'Exception type: {exc_type}')
            print(f'An error occurred: {exc_value}')
            print(f'Traceback: {traceback}')


        return False

        
        
        
        

with FileManager('lezione_15/esercizi_context_manager/example.txt', 'r') as file:

    output: str = file.read()
    print(output)

    

