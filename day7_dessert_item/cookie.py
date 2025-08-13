from dessertitem import DessertItem


class Cookie(DessertItem):

    def __init__(self,units):
        super().__init__("Cookie")
        self.units=units
        self.price = (10/12)*self.units

    def costOfItem(self):
        return self.price

    def __str__(self):
        return f"{self.name}  -  {self.costOfItem()} "
