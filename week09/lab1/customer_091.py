class Customer(object):

    discount = 0

    def __init__(self, name, balance, addr_line1, addr_line2, addr_line3):
        self.name = name
        self.balance = balance
        self.addr_line1 = addr_line1
        self.addr_line2 = addr_line2
        self.addr_line3 = addr_line3

    def owes(self):
        return self.balance - self.balance * self.discount // 100

    def __str__(self):
        l = [self.name, self.addr_line1, self.addr_line2, self.addr_line3]
        l.append("Balance: {:.2f}".format(self.balance))
        l.append("Discount: {}%".format(self.discount))
        l.append("Amount due: {:.2f}".format(self.owes()))
        return "\n".join(l)

class ValuedCustomer(Customer):
    discount = 10
