from desertItems import DesertItem

class Cookies(DesertItem):
    def __init__(self,name,qty):
        super().__init__(name)
        self.qty = qty

    def costOfItem(self):
        return (self.qty/12)*10