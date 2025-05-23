class User:

    def __init__(self, first_name, last_name, role, login_attemps = 0):

        self.first_name = first_name
        self.last_name = last_name
        self.role = role.lower()
        self.login_attempts = login_attemps
    
        

    def describe_user(self):
        print(f'User info: \nFirst name: {self.first_name}\nLast name: {self.last_name}\nRole: {self.role}')

    def greet_user(self):
        if self.role == 'admin':
            print('hello admin!, you want to see some data?')
        elif self.role == 'user':
            print(f'hello {self.first_name} {self.last_name}')
    
    def increment_login_attempts(self, login):

        self.login_attempts += 1

    def reset_login_attempts(self):

        self.login_attempts = 0
    
        
    
popa = User('Alessando', 'Popa', 'ADmin')
pier = User('Pier', 'Damien ramillano rabong', 'USER')

pier.describe_user()
pier.greet_user()

popa.describe_user()
popa.greet_user()