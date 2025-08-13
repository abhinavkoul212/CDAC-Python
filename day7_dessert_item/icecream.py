from dessertitem import DessertItem


class IceCream(DessertItem):

    def __init__(self,units):
        super().__init__("IceCream")
        self.units=units
        self.cost= 50*units


    def costOfItem(self):
        return self.cost

    def __str__(self):
        return f"{self.name}  -  {self.costOfItem()}"