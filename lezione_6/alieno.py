class Alieno:

    

    '''

    Di un alieno ci interessa sapere la galassia di provenienza
    self.galaxy: str

    '''
    
    # inzializzare un oggetto della classe alieno

    def __init__(self, galaxy: str):
        
        self.setGalaxy(galaxy)

    # definire metodo per impostare il valore dell'attributo self.galaxy

    def setGalaxy(self, galaxy: str):

        if galaxy:

            self.galaxy  = galaxy

        else:

            print('Errore la galassia non puo essere una stringa vuota!')
        
    # definire un metodo per restituire  il valore dell'attributo self.galaxy
    
    def getGalaxy(self) -> str:
        return self.galaxy
    
    # definire un metodo speak()

    def speak(self) -> None:

        print('ciao sono popa   ')

    def __str__(self) -> str:

        return f'Alieno proveniente dalla galassia {self.getGalaxy()}'
        
    