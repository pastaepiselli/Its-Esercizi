class Account:
    def __init__(self, account_id) -> None:
        self.account_id = account_id
        self.balance = 0.0
    def deposit(self, amount):
        self.balance += amount
    def get_balance(self):
        return self.balance

class Bank:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, account_id):
        if account_id in self.accounts:
            raise KeyError("Account with this ID already exists")
        self.accounts[account_id] = Account(account_id)
    
    def deposit(self, account_id, amount):
        self.accounts[account_id].deposit(amount)
    
    def get_balance(self, account_id):
        if account_id in self.accounts:
            return self.accounts[account_id].get_balance()
        raise KeyError("Account not found")