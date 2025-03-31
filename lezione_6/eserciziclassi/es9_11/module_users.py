class User:

    def __init__(self, first_name, last_name, username, email):

        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    def describe_user(self):
        print (f'First name: {self.first_name}\nLast name: {self.last_name}\nUsername: {self.username}\nEmail: {self.email}')
        

class Privileges:

    def __init__(self, privileges):

        self.privileges: list = privileges

    def show_privileges(self):

        print(*self.privileges)


class Admin:

    def __init__(self, user, privileges):

        self.user = user
        self.priviileges = privileges
                