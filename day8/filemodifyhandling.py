# def fileCheck():
#     f= open("def.txt","a")
#     f.write("Hello")
#     print("Opening again")
#
# f=open("def.txt","w")
# f.write("abc")
# fileCheck()
# f=open("def.txt","a")
# f.write("def")
#
# f=open("def.txt","r")
# data = f.read()
# print(data)







#####################################################
# f=open("def.txt","r")
# data=f.read()   #f.read() has already reached end of line
# print(data)
# print("read till end of line",f.read()) # hence nothing read from file
# f.seek(0)    # to bring file pointer to a particular location
# string1=f.read()
# print(string1)
# f.close()






###############################################################
#import re------------------------pending

# file=open("def.txt","w")
# file.write("# This is Python. \n Hello, my name is Abhinav.")
# file.close()
#
# file1=open("def.txt","r")
# data_string= file1.read()
# file.close()
# print(data_string)




#filter the string from file removing # ,. space and \n from string and find count of words---------------pending





############
# writing object to file
#error was there
#reference write karega when tried with bw and object
#then write and str(e) tried
#so change made in Employee class and def __str__ ...returns  string empidId+.......
#file import and object taken for Employee

#file.open("obj.txt","w")
#file.write(str(e))

#file.close()



##################################################################


def Summary(str):
    print(str)
    count=1
    for i in range(0,len(str),1):
        if str[i] == "\n":
            count += 1
    print(count)




file=open("def.txt","r")
data =file.read()
# file.write("# This is Python. \n Hello, my name is Abhinav.")
file.close()
Summary(data)









