from dessertitem import DessertItem

class Candy(DessertItem):

    def __init__(self,weight):
        super().__init__("Candy")
        self.price=50
        self.weight=weight/1000

    def costOfItem(self):
        return  (self.price*self.weight)

