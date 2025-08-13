
class Catr:
    productId = 0
    productName = []
    totalQuantity = 0
    price =0

    def __init__(self,productName,price):
        self.productId = self.productId + 1
        self.productName = self.productName.append(productName)
        self.totalQuantity= self.totalQuantity +1
        self.price = self.price + price

    def showProducts(self):
        return self.productName

    def showPrice(self):
        return self.price

    def showQuantity(self):
        return self.totalQuantity



