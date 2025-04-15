class Persona:
    # i dati di persona sono vuoti
    def __init__(self, name: str, lastname: str, age: int):
        # richiamo il set nell'init per avere anche un controllo del dato
        self.set_name(name)
        self.set_lastname(lastname)
        self.set_age(age)

    def __str__(self):

        return f'Persona {self.name}, {self.lastname}, {self.age}'
        
    def __call__(self, *args, **kwds):
        if self.age < 18:

            print(f'{self.name} {self.lastname} e minorenne')

        elif 18 <= self.age <30:

            print(f'{self.name} {self.lastname} e maggiorenne')

        elif 30 <= self.age < 80:

            print(f'{self.name} {self.lastname} e una persona adulta')
        
        else:

            print(f'{self.name} {self.lastname} e una persona anziana')

    # funzioni con set prendono paremetri in input 
    def set_name(self, name):
        if name:
            self.name = name
        else:
            print('Errore il nome non puo essere una stringa vuota')
        
    def set_lastname(self, lastname: str):
        if lastname:

            self.lastname = lastname
        
        else:
             print('Errore il cognome non puo essere una stringa vuota')    
    
    def set_age(self, age: str):
        if age < 0 or age > 130:
            self.age = 0
        else:
            self.age = age
    # non ha nessu input ma ritorna un valore
    def get_name(self):
        return self.name
    
    def get_lastname(self):
        return self.lastname
    

    def get_age(self):
        return self.age
