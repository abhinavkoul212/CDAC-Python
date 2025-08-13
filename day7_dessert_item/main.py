from candy import Candy
from day7_dessert_item.checkout import CheckOut
from day7_dessert_item.cookie import Cookie
from day7_dessert_item.icecream import IceCream


class Main:
    checkout = CheckOut()
    while(True):

        print("Dessert Store")
        print("1. Candy ")
        print("2. Cookie ")
        print("3. Ice Cream")
        print("4. EXIT")
        print("5. No.of items in CashRegister")
        print("6. Total cost of Cart")
        print("7. Clear the cart/cash Register")
        choice=int(input("Enter the choice : "))

        match choice:

            case 1:
                weight=int(input("Enter the weight in grams:"))
                candy = Candy(weight)
                checkout.addToCart(candy)

            case 2:
                units=int(input("Enter the no. of cookie units :"))
                cookie = Cookie(units)
                checkout.addToCart(cookie)

            case 3:
                units = int(input("Enter the no. of icecream units :"))
                icecream = IceCream(units)
                checkout.addToCart(icecream)

                #break--- not required in python
                # languages like c/java have fall through behaviour and hence need break
            case 4:
                #lets print the cash register here before she exits the system
                #checkout.finalCheckout()
                dict1=checkout.__repr__()
                for key in dict1.keys():
                    print(f"{key} - {dict1[key]}")
                exit(0)

            case 5:
                #for get no of items
                print(checkout.getNoOfItemInCart())

            case 6:
                #for total cost of cart
                print(checkout.getTotalCostOfCart())
            case 7:
                #for clearing the cart
                checkout.clearCart()
            case _:
                print("Invalid Output!!!!  Try again")
                continue

