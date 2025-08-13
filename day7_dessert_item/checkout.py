class CheckOut:

    cashRegister=list()

    def addToCart(self,dessertItem):
        self.cashRegister.append(dessertItem)
        # # for i in self.cashRegister:-------------this will print reference only
        # #     print(i)
        #     #---------can it return details to be printed on console---pending
        # #lets iterate first here
        # for i in self.cashRegister:
        #     print()
        print("Items in Cart: ")
        for item in self.cashRegister:
            print(item)

    # def finalCheckout(self):
    #     print("Items in cart:")
    #     for item in self.cashRegister:
    #         print(item)


    def getNoOfItemInCart(self):
        if len(self.cashRegister) !=0:
         return len(self.cashRegister)
        else:
            return f"Mann kaa radio bhajne de zara"

    def getTotalCostOfCart(self):
        total=0
        for i in self.cashRegister:
            total=total+i.costOfItem()
        return total

    def clearCart(self):
        if len(self.cashRegister) == 0:
            print("List is empty")
        else:
            self.cashRegister.clear()
        for item in self.cashRegister:
            print("I am here")
            print(item)
        #print("entire cart/cash register is empty now2")



    def __repr__(self):
        #this logic can be written in str also for that calls are over and again
        #here we are storing in dict and then returning
        invoice={}
        for i in self.cashRegister:
            invoice[i.NameOfItem()]=i.costOfItem()
        invoice["Total"] = self.getTotalCostOfCart()
        return invoice


