from candy import Candy
from cookies import Cookies
from iceCream import IceCream
from sundae import Sundae
from dbCart import Cart

class Store:

    choice = True
    cart = Cart()
    try:
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
                    print("\n Cart Summary",cart)
                    cart.clearCart()
                case 1:
                    qty = int(input("Enter quantity"))
                    item = Candy("Candy",qty)
                    cart.addToCart(item)
                case 2:
                    qty = int(input("Enter quantity"))
                    item = Cookies("Cookies", qty)
                    cart.addToCart(item)
                case 3:
                    qty = int(input("Enter quantity"))
                    print("Add Toppings")
                    print("1. Yes")
                    print("2. No")
                    toppingChoice = int(input("Enter your choice"))
                    if toppingChoice == 1:
                        item = IceCream("IceCream", qty)
                        cart.addToCart(item)
                    elif toppingChoice == 2:
                        item = Sundae("IceCream", qty)
                        cart.addToCart(item)
                    else:
                        print("Invalid Choice --------> not adding toppings")
                        item = IceCream("IceCream", qty)
                        cart.addToCart(item)
                case _:
                    print("Invalid please enter a valid choice")
    finally:
        print("\n Closing Database Connection")
        cart.close()

