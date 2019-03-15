class BankAccount(object):

    def __init__(self, balance=0):
        self.balance = float(balance)

    def deposit(self, arg):
        self.balance += arg

    def withdraw(self, arg):
        if self.balance - arg >= 0:
            self.balance -= arg
        else:
            print("Insufficient funds available")

    def __str__(self):
        return "Your current balance is: {:.2f} euro".format(self.balance)
