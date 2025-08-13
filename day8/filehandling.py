
# f=open("abc.txt","w")
# f.write("Hello")
# f.close()
#
try:
    f=open("def.txt","r")
except Exception :
    print("File doesn't exist")
    f = open("def.txt", "w")
    f.write("Bingo \n Vikas")
    f.close()

finally:
    f = open("def.txt", "r")
    data = f.read()
    f.close()
    print(data)

f=open("def.txt","a")
f.write("   # This , is Python file handling.")
f.close()

f=open("def.txt","r")
str=f.read()
f.close()

print(type(str))

list1=str.split(" ")
listnew=[]
for word in list1:
    listnew.append(word.capitalize())
print(listnew)

stringnew=" ".join(listnew)
print(stringnew)

f=open("def.txt","w")
f.write(stringnew)
f.close()

f=open("def.txt","r")
str=f.read()
print(str)


f=open("def.txt","r")
data=f.read()
f.close()
print(data)