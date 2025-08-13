# recursion
def fact(num):
    if (num == 1):
        return 1
    return num*fact(num-1)

def add(a,b):
    #print(a," + ", b)
    print(f"the value of a is: {a}  and the value of b is :{b}")
    return a+b