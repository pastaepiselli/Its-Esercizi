class BankAccount:
    def __init__(self, saldo=0) -> None:
        self.balance = saldo
    def deposit(self, amount) -> None:
        self.balance += amount
    def withdraw(self, amount) -> None:
        if amount > self.balance:
            raise ValueError
        self.balance -= amount
       