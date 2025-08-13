from desertItems import DesertItem

class Candy(DesertItem):
    def __init__(self, name, qty):
        super().__init__(name)
        self.qty = qty

    def costOfItem(self):
        return (self.qty/1000)*50


