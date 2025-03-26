class Persona:
    # i dati di persona sono vuoti
    def __init__(self):
        self.name = ""
        self.lastname = ''
        self.age = 0

    def display_data(self):
        print(f'Name: {self.name}, LastName: {self.lastname}, age: {self.age}') 
    
    # funzioni con set prendono paremetri in input 
    def set_name(self, name):
        self.name = name
       
    def set_lastname(self, lastname: str):
        self.lastname = lastname
    
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
ln: Persona = Persona()



ln.display_data()
ln.set_name("palle culo")
ln.display_data()
ln.set_lastname("cutolo")
ln.display_data()
ln.set_age(28)
ln.display_data()