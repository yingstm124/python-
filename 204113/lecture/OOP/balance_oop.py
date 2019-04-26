class account (object):
    def __init__(self, n, b=0):
        self.name = n
        self.balance = b

    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return True

    def withdrow(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            return True
        else:
            return False

    def transfer(self, account, amount):
        if (self.balance -  amount) < 0:
            return False
        else:
            self.withdrow(amount)
            account.deposit(amount)
            return True
    
    def print_account(self):
        print("Account Name : {0}".format(self.name))
        print("Account Balance : {0:.2f}".format(self.balance))


a = account("Alice")
b = account("Bob")

a.deposit(150)
a.transfer(b,15)

a.withdrow(20)
a.print_account()



