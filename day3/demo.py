#
# print("Hello World")
# a=3
# b=4
def add(a,b):
    print(a)
    return a+b

# print(add(a,b))
# print(add("Hello","World"))
#issue arises with     add("Hello",1)     data type mismatch
#even odd
#fact
#prime

def fact(num):
    sum=1
    while(num>0):
        sum=sum*num
        num=num-1
        add(num,sum)
    return sum


num=int(input("Enter the number:"))
sum=fact(num)
print(sum)











#even ODD


# def isEvenOrOdd(inpt):
#     if (inpt%2==0):
#         return "Even"
#     else:
#         return "Odd"
#
#
#
# inpt=int(input("Enter the number:"))
# x=isEvenOrOdd(inpt)
# print(x)







#prime number

# def isPrime(inpt):
#     if(inpt<=1):
#         return False
#     else:
#         for i in range(2,int(inpt*0.5)):
#               if(inpt%2==0):
#                   return False
#        return True
#
# inpt=int(input("Enter the number:"))
# x=isPrime(inpt)
# print(x)


#named parameters

# def add(a=0,b=0):
#     print(a)
#     print(b)
#     return a+b
#
# print(add(b=12,a=10))
# print(add(a=1))



# def add(variable):
#    sum=0
#    for item in variable:
#         sum=sum+item
#    return sum
#
# print(add([12,10]))
# #print(add(1,12,14))



# def add(name,*args):
#    print(name)
#    sum=0
#    for item in args:
#         sum=sum+item
#    return sum
#
# print(add("string",12,10))
# #print(add(1,12,14))




#lambda/ anonymous functions
#
# add=lambda a,b:a+b
# sub=lambda a,b:a-b
#
# print(add(1,2))

######lambda function for prime number is pending




#list comprehension
# x=[i for i in range(1,100) if i%2==0]
# print(x)






# def conv(str):
#     str1 = ""
#     if('_' in str):
#         str1 += str[0].upper()
#         for i in range(1,len(str)):
#             if(str[i-1]=="_"):
#                 str1 += str[i].upper()
#                 i += 2
#             elif(str[i] != '_'):
#                 str1 += str[i]
#     else:
#         print("AA")
#     return  str1
#
# print(conv("bc_ef"))
