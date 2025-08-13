from dessertitem import DessertItem

class CheckOut:

    cashRegister = list()

    def showCart(self):
        for item in self.cashRegister:
            print(item.NameofItem(), " : ", item.costOfItem())

    def addToCart(self,dessertItem):
        self.cashRegister.append(dessertItem)

    def getNoOfItemInCart(self):
        return len(self.cashRegister)
    def getTotalCostOfCart(self):
        total = 0
        for i in self.cashRegister:
            total = total+i.costOfItem()
        return total

    def clearCart(self):
        self.cashRegister.clear()

    def __repr__(self):
        invoice = {}
        for i in self.cashRegister:
            invoice[i.NameofItem()] = i.costOfItem()
        invoice["Total"] = self.getTotalCostOfCart()
        return str(invoice)

