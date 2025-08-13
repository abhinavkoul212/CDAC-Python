from dessertitem import DessertItem


class IceCream(DessertItem):

    def __init__(self,icecreamunits):
        super().__init__("IceCream")
        self.icecreamunits=icecreamunits
        self.cost= 50* icecreamunits


    def costOfItem(self):
        return self.cost