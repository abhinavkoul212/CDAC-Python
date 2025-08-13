from dessertitem import DessertItem


class Cookie(DessertItem):

    def __init__(self,cookieunits):
        super().__init__("Cookie")
        self.cookieunits=cookieunits
        self.price = (10/12)*self.cookieunits

    def costOfItem(self):
        return self.price
