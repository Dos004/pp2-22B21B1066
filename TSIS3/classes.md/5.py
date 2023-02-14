class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("withdrawal amount exceeds available balance.")
    
    def __str__(self):
        return f"aAccount owner: {self.owner}\naAccount balance: ${self.balance}"

my_account = BankAccount("Alice", 100)
print(my_account)  # is should output "Account owner: Alice\nAccount balance: $100"