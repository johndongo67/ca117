class BankAccount(object):

    next_account_number = 16555232

    total_lodgements = 0

    interest_rate = 0.043

    def __init__(self, forename, surname, balance=0):
        self.forename = forename
        self.surname = surname
        self.balance = balance
        self.account_number = BankAccount.next_account_number
        BankAccount.total_lodgements += 1
        BankAccount.next_account_number += 1

    def lodge(self, arg):
        self.balance += arg
        BankAccount.total_lodgements += 1

    def apply_interest(self):
        self.balance += self.balance * BankAccount.interest_rate

    def __iadd__(self, other):
        z = other + self.balance
        self.balance = z
        return self

    def __str__(self):
        return "Name: {}\nAccount number: {}\nBalance: {:.2f}".format(self.forename + " " + self.surname, self.account_number, self.balance)
