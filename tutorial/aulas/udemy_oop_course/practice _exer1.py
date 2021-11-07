'''
Make a class that represents a bank account. Create four methods named set_details, display, withdraw and 
deposit.

In the set_details method, create two instance variables : name and balance. The default value for balance 
should be zero. In the display method, display the values of these two instance variables.

Both the methods withdraw and deposit have amount as parameter. Inside withdraw, subtract the amount from 
balance and inside deposit, add the amount to the balance.

Create two instances of this class and call the methods on those instances.
'''



class BankAccount:
    def __init__(self, name = 'default', balance = 0):
        self.name = name
        self.balance = balance

    def set_details(self, name, balance):
        self.name = name
        self.balance = balance
    
    def display(self):
        print(f'Name: {self.name}')
        print(f'Balance: {self.balance}')
    
    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount



user_account = BankAccount()
user_account.set_details('John', 100)
user_account.display()


