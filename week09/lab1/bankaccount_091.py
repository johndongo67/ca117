class BankAccount(object):

    account_type = "General"
    next_account_number = 16555232

    def __init__(self, forename, surname, balance):
        self.forename = forename
        self.surname = surname
        self.balance = balance
        self.next_account_number = BankAccount.next_account_number
        BankAccount.next_account_number += 1

    def lodge(self, arg):
        self.balance += arg

    def withdraw(self, arg):
        if self.balance - arg >= 0:
            self.balance -= arg
        else:
            print("Insufficient funds available")

    def __str__(self):
        name = self.forename + " " + self.surname
        return "Name: {}\nAccount number: {}\nAccount type: {}\nBalance: {:.2f}".format(name, self.next_account_number, BankAccount.account_type, self.balance)


class CurrentAccount(BankAccount):

    overdraft = -1000.00
    account_type = "Current"

    def withdraw(self, arg):
        if self.balance - arg >= CurrentAccount.overdraft:
            self.balance -= arg
        else:
            print("Insufficient funds available")

    def __str__(self):
        name = self.forename + " " + self.surname
        return "Name: {}\nAccount number: {}\nAccount type: {}\nBalance: {:.2f}\nOverdraft: {:.2f}".format(name, self.next_account_number, CurrentAccount.account_type, self.balance, CurrentAccount.overdraft)

class SavingsAccount(BankAccount):

    interest_rate = 0.01
    account_type = "Savings"

    def apply_interest(self):
        self.balance += self.balance * SavingsAccount.interest_rate

    def __str__(self):
        name = self.forename + " " + self.surname
        return "Name: {}\nAccount number: {}\nAccount type: {}\nBalance: {:.2f}\nInterest rate: {}".format(name, self.next_account_number, SavingsAccount.account_type, self.balance, SavingsAccount.interest_rate)
