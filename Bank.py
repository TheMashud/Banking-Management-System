class Bank:
    def __init__(self, name, Adress) -> None:
        self.name = name
        self.Adress = Adress
        self.Total_balance = 0
        self.Total_loan_amount = 0
        self.transaction_history = []
        self.loan_feature_enable = True

    def total_available_balance(self):
        return self.Total_balance
    
    def total_loan_amount(self):
        return self.Total_loan_amount
    
    def enable_loan(self):
        self.loan_feature_enable = True

    def disable_loan(self):
        self.loan_feature_enable = False

    def add_transaction(self, transaction):
        self.transaction_history.append(transaction)
    
    def __repr__(self) -> str:
        print(self.name, self.Adress)

class User:
    def __init__(self, name, email, addrees, password) -> None:
        self.name = name
        self.email = email
        self.address = addrees
        self.__password = password
        self.balance = 0
        self.loan_amount = 0
        self.transaction_history = []

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, value):
        self.__password = value

    def Crate_account(self, name, email, addrees, password ):
        self.name = name
        self.email = email
        self.address = addrees
        self.__password = password
    
    def Cheak_balance(self):
        return self.balance
    
    def get_transaction_history(self):
        return self.transaction_history
    
    def take_loan(self):
        if self.balance > 0:
            self.loan_amount = 2* self.balance
            self.balance += self.loan_amount
            self.transaction_history.append((f"Loan Taken: {self.loan_amount}"))
            return True
        return False
    
    def deposit(self, bank, amount):
        if amount > 0:
          self.balance = amount + self.balance
          self.loan_amount = self.balance * 2
          bank.Total_balance = amount + bank.Total_balance
          transaction = Transaction(self.name, self.name, amount)
          return True
        return False


    
    def withdrawal_amount(self, bank, amount):
        if amount > 0 and amount <= self.balance and amount <= bank.Total_balance:
            self.balance -= amount
            bank.Total_balance -= amount
            transaction = Transaction(self.name, self.name, -amount)
            self.transaction_history.append(transaction)
            return True
        elif amount > bank.Total_balance:
            print("Bank is bankrupt. Unable to withdraw.")
        return False
    
    def take_loan(self, bank, amount):
        if bank.loan_feature_enable and amount <= self.loan_amount and amount > 0 and amount <= bank.Total_balance:
            self.balance += amount
            bank.Total_loan_amount += amount
            bank.Total_balance -= amount
            transaction = Transaction(self.name, self.name, amount)
            self.transaction_history.append(transaction)
            bank.add_transaction(transaction)
            return True
        return False
    
    def get_transaction_history(self):
        return self.transaction_history

        
class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

class Admin:
    def __init__(self, bank):
        self.bank = bank

    def Crate_an_account(self, name, email):
        self.name = name
        self.email = email

    def total_available_balance(self):
        return self.bank.total_available_balance()

    def total_loan_amount(self):
        return self.bank.total_loan_amount()

    def enable_loan_feature(self):
        self.bank.enable_loan()

    def disable_loan_feature(self):
        self.bank.disable_loan()

    def get_transaction_history(self):
        return self.bank.transaction_history




islami_bank = Bank("Islami Bank", 'Chittagong')

opi = User('Mashudul joque', '23@miql.com', 'ctg', 1234)
opi.deposit(islami_bank, 30000)
print(opi.Cheak_balance())
opi.withdrawal_amount(islami_bank, 2000)
print(opi.Cheak_balance())
opi.take_loan(islami_bank, 20000)
print(opi.Cheak_balance())

