from dbConnectSQL import Database

class Cart:
    def __init__(self):
        self.db = Database()

    def addToCart(self,item):
        name = item.getName()
        qty = item.qty
        price = item.costOfItem()
        self.db.insertToCart(name,qty,price)

    def shohAll(self):
        print(self.db.showCart())


    def totalCost(self):
        data = self.db.showCart()
        return sum(item[3] for item in data)

    def clearCart(self):
        self.db.clearCart()

    def close(self):
        self.db.close()

    def __repr__(self):
        cartTotal = {}
        data = self.db.showCart()
        for item in data:
            name,qty,price = item[1],item[2],item[3]
            if(name in cartTotal):
                cartTotal[name] += price
            else:
                cartTotal[name] = price
        cartTotal['Total Cost']=self.totalCost()
        return str(cartTotal)
