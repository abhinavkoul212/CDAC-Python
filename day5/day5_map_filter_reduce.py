########## return new list numbers greater than num
from functools import reduce

# def func(list1,num):
#     listnew=[]
#     for x in list1:
#         if x> num:
#             listnew.append(x)
#     return listnew
#
#
# list1=[1,5,7,9,11]
#
# print(func(list1,5))

#########################  any logical op on list square################
# def func(list1):
#      listnew=[x*x for x in list1]
#      return listnew
#
#
# list1=[1,5,7,9,11]
#
# print(func(list1))
# def func(num):
#     return num*num

# list1=[1,4,7,9,10]
# #y= [func(i) for i in list1]
# #print(y)
# #x=list(map(func,list1))-------------------func can be replaced with lambda expression
# # list(x)
#
#
# x=list(map(lambda num:num*num,list1))
# print(x)

# list1=[2,3,4,5,6,7]
# list2=[7,8,9,9,3,7]
#
# x= list(map(lambda  a,b:a+b,      list1,list2))
# print(x)
#
# list1 = [2, 3, 4, 5, 6, 7]
# list2 = [7, 8, 9,  7]
# list3 = [7, 8, 9, 9, 3]
#
# x = list(map(lambda a, b,c: a + b+c, list1, list2,list3))
# print(x)
#
#
#
#
# list1 = [2, 3, 4, 5, 6, 7]

# def func(num):
#     if  num>5:
#         return True
#     else:
#         return False
#
# x=filter(func,list1)
# print(list(x))
# ############ whats the utility list comprehension can be used too
# x=filter(lambda num:num > 5 ,list1)
# print(list(x))

# filter using list comprehension????????????
#
#
# list1 = [2, 3, 4, 5, 6, 7]
#
# def add(a,b):
#     return a+b
# x= reduce(add,list1)
# print(x)

####y=[for i in list1] ----- will get called every time


# list1=[1,5,7,3,9]
# list2=[9,1,3,5]
#
# list1.sort()
# list2.sort()

# def comp(num1,num2):-------------pending
#
#
# x=list(map(comp ,list1,list2))
# print(x)


#
#
# String1="Hello world how are you"
#
# list1=String1.split(" ")
# print(list1)
#
# def func(name):
#     newlist=[]
#     count=0
#     newlist.append(name.upper())
#     newlist.append(name.lower())
#     newlist.append(len(name))
#     return newlist
#
#
#
#
# x=list(map(func,list1))
# for i in x:
#     print(i)










