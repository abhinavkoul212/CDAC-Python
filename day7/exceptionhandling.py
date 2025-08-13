#generally we handled errors by ptting on cndition check uing if else but there are many ambiguities with that
#refer notes.......hence try except

#   old way of error handling
# a="10"
# b="2n"
# # condition check
# if a.isnumeric() and b.isnumeric():
#     c=int(a)+int(b)
# else:
#     print("Input parameter mismatch...Number Format exception")
# x=10
# try:
#  x/0
# except ZeroDivisionError:
#     print("Zero Error")
# except ArithmeticError:
#     print("Error !!!!!")
#
# else:
#     print("No exception")
# finally:
#     print("Execution despite error")



##### divide by zero ....arithmetic issue
# a=10
# b=0
# try :
#     c=a/b
# except ZeroDivisionError :
#     print("Divide by Zero Error")
# except ValueError:
#     print("value error'")
# except:
#     print("All handled here...ut hiearchy is maintained")
# else:
#     print(c)
# finally:
#     print("Anyhow gets executed...erroror n error...perhaps for closing files and db connections....external resources...like payment gateway connections etc.")



#######Number format issue


# a="10"
# b="2n"
#
# try:
#     c=int(a)+int(b)
# except Exception:
#     print("Input parameter mismatch...Number Format exception")
# else:
#     print(c)
# finally:
#     print("ANyhow executed")



#Array index out of bounds

list1=[10,20,30]
try:
    x=list1[0]
except:
    print("Out of bounds index error")
finally:
    print("Anyhow executed")


print(x)




