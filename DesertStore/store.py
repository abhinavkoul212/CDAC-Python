from desertItems import DesertItem
from candy import Candy
from cookies import Cookies
from iceCream import IceCream
from sundae import Sundae
from cart import Cart

class Store:

    choice = True
    cart = Cart()

    while choice:

        print("\n Desert Items:")
        print("1. Candy")
        print("2. Cookies")
        print("3. IceCream")
        print("0. Exit")
        ch =int(input("Enter Your choice"))

        match ch:
            case 0:
                choice = False
                print("\n",cart)
            case 1:
                qty = int(input("Enter quantity"))
                item:DesertItem = Candy("Candy",qty)
                cart.addToCart(item)
            case 2:
                qty = int(input("Enter quantity"))
                item: DesertItem = Cookies("Cookies", qty)
                cart.addToCart(item)
            case 3:
                qty = int(input("Enter quantity"))
                print("Add Toppings")
                print("1. Yes")
                print("2. No")
                toppingChoice = int(input("Enter your choice"))
                if toppingChoice == 1:
                    item: DesertItem = IceCream("IceCream", qty)
                    cart.addToCart(item)
                elif toppingChoice == 2:
                    item:DesertItem = Sundae("IceCream", qty)
                    cart.addToCart(item)
                else:
                    print("Invalid Choice --------> not adding toppings")
                    item: DesertItem = IceCream("IceCream", qty)
                    cart.addToCart(item)
            case _:
                print("Invalid please enter a valid choice")


