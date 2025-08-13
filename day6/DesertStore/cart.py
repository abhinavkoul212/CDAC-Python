class Cart:

    cashRegister = []

    def addToCart(self,item):
         self.cashRegister.append(item)

    def totalCost(self):
        totPrice = 0
        for item in self.cashRegister:
            totPrice = totPrice + item.costOfItem()
        return totPrice

    def clearCart(self):
        self.cashRegister.clear()

    def __repr__(self):
        cartTotal = {}
        for item in self.cashRegister:
            if(item.getName() in cartTotal.keys()):
                cartTotal[item.getName()] = cartTotal[item.getName()] + item.costOfItem()
            else:
                cartTotal[item.getName()]=item.costOfItem()
        cartTotal['Total Cost']=self.totalCost()
        return str(cartTotal)
