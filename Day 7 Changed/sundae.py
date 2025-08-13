from icecream import IceCream


class Sundae(IceCream):

    def __init__(self,unit,topping):
        super().__init__(unit)
        if  topping==1: ###nuts
            self.price=super().costOfItem()+50
        elif topping ==2:
            self.price=super().costOfItem()+100
        elif topping ==3:
            self.price=super().costOfItem()+200
        else:
            self.price=super().costOfItem()

    def costOfItem(self):
        return self.price



