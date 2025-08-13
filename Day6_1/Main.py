from manager import Manager
from marketingExe import MarketingExe
m1 =  Manager(1,"manager1",3424343)
m2= Manager(2,"manager2",3420000)
m3= Manager(3,"manager3",3420000)
#m1.printEmp()

me1 = MarketingExe(12,"Marketing executive 1",154456456)
me2 = MarketingExe(13,"Marketing executive 2",154456000)
me3 = MarketingExe(14,"Marketing executive 2",154456023)
#me1.printEmp()


''' print(type(me))
 str = str(type(me))
 print(str,"this is string")
 if("MarketingExe" in str):
     print("Executive found")
 print(type(m))'''


# ---------------------------------------------------->Pending
lst= [m1,m2,m3,me1,me2,me3]
lst1=[]
lst2=[]
lst3=[]

for o in lst:
    str1 = str(type(o))
    if ("MarketingExe" in str1):
     lst1.append(o)
    elif("Manager" in str1):
        lst2.append(o)
    else:
        lst3.append(o)

print("Main List ----->",lst)
print("Manager List ------->",lst1)
print("Marketing Executive List------->",lst2)
print("Employee List ----> ",lst)



