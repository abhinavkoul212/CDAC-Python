from desertItems import DesertItem

class IceCream(DesertItem):
    def __init__(self,name,qty):
        super().__init__(name)
        self.qty = qty

    def costOfItem(self):
        return self.qty*30