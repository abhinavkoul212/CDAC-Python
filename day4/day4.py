################# tried for Debugging #############
#import factt
from factt import fact
# def add(a,b):
#     print(a)
#     return a+b

# def fact(num):
#     sum=1
#     while(num>0):
#         sum=sum*num
#         num=num-1
#         add(num,sum)
#     return sum



# num=int(input("Enter the number:"))
# sum=factt.fact(num)
# print(sum)
# print(factt.add(9,9))


############################ List Comprehension ####################################

# x={i for i in range(1,11,1)}
# print(x)

# x=[i for i in range(1,11,1)]
# print(x)
#
# x=(i for i in range(1,11,1))----generator ???????
# print(x)


# x=[i for i in range(1,11,1) if i%2==0]
# print(x)


# x={fact(i) for i in range(1,11,1)}
# print(x)

#
# l=[]
# for i in range(1,11):
#     l.append(fact(i))
# print(l)


# x=[i for i in range(1,100) if i%2==0]
# print(x)
#
# x=[i for i in range(1,100) if i%2!=0]
# print(x)
#

#----------------------------------------------------------------------------->>>>>> PENDING

# def countvowels(name):
#     count =0
#     for i in name:
#         print(i)
#         # if( i.lower()== 'a' or i.lower() =='e' or i.lower() == 'i' or i.lower() =='o' or i.lower() == 'u'):
#         #     count = count +1
#     print(count)
#     return count
#
# names = ["Abhinav", "Akhilesh", "Ajinkya", "Vikas"]
# #
# # temp = [name for name in names if name.startswith("A")]
# #
# temp = [name for name in names if countvowels(names)>=2]
# print(temp)


# str1 = "Vikas Singh is very kind"
#
# v = ['a','e','i','o','u','A','E','I','O','U'];
#
# str2 =""
#
# for str in str1:
#     if( str not in v):
#         if(str != ' '):
#             str2 = str2+str+'o'+str
# print(str2)

# ------------------------------------------------------>>>>>Pending

names = ["Abhinav", "Akhilesh", "Ajinkya", "Vikas"]
def checkLen(lst,n):
    res = []
    for i in lst:
        if(len(i)>=n):
            res.append(i)
    return res

print(checkLen(names,8))


# l = [1,2,3,4,5,6,7,8,9,0]
#
# x= iter(l)
#
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
#
# print("---------------------------")
#
# for i in x:
#     print(i)


# s = "Hello"
# l=[10,28,1,12,67,33,3]
#
# # print(len(s))
# # print(len(l))
# #print(sorted(l))
# #print(reversed(l))  ----------------------->> Not  Working
# y=l.sort(reverse=True)
# print(y)              # ------not working

# d=set(l)
# print(d)


# list1=['R','a','m']

# list2=[3,1,9,10]

# y=list2.sort()
# print(y)
#
#
# print(sorted(list2))
#
#
# a= int("1")
# print(a)
#
# b=str(10)
# print(b)

# list2=[3,1,9,10]
# min =list2[0]
# max = list2[0]
# for l in list2:
#     if(l>max):
#         max=l
#     if(l<min):
#         min=l
# print("Min:", min, " Max:",max)