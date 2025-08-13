from candy import Candy
from checkout import CheckOut
from cookie import Cookie

checkout=CheckOut()

while(True):
    print("Dessert Store")
    print("1. Candy ")
    print("2. Cookie ")
    print("3. Ice Cream")
    print("0. EXIT")
    choice = int(input("Enter the choice : "))

    if choice == 1:
        print("In Candy")
        weight = int(input("Enter the weight in grams:"))
        can = Candy(weight)
        checkout.addToCart(can)
    elif choice == 2:
        num = int(input("Enter the number of units for cookie: "))
        coo = Cookie(num)
        checkout.addToCart(coo)
    elif choice == 3:
        pass
    elif choice == 0:
        break
    else:
        print("Invalid Input")

print(checkout)