

class store(object):
    def __init__(self, n, stock=0, income=0):
        self.name = n
        self.stock = stock
        self.income = income
     
    
    def load_product(self, n, amount):
        n.stock += amount
        
    def sell(self, n):
        if (self.stock-1) < 0:
            return False
        else:
            self.income += n.profit()
            return True
    
    def total_income(self):
        print("incom {0}".format(self.income))


    
class product(store):

    def __init__(self, n, sp=0, fp=0):
        self.name = n
        self.stock_price = sp
        self.final_price = fp

    def profit(self):
        profit = self.final_price - self.stock_price 
        print("Profit is {0:.2f}".format(profit))
        return profit

    
    
store = store("Am")

banana = product("Banana", 10, 20)
apple = product("Apple", 50, 150)

store.load_product(banana, 1)
store.load_product(apple, 1)

store.sell(banana)
store.sell(banana)
store.sell(banana)
store.sell(banana)
store.sell(apple)

store.total_income()



