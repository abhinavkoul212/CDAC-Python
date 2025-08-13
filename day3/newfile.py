# import demo   #basic import
# import  demo as f   #import with rename
# from demo import add   # specific import  better way to import not much memory consumed
#
# print(demo.add(1,2))
# print(f.add(10,20))
# print(add(5,6))

# not juxt lambda but concretely written function can be imported as well




###### Two Strings are Anagram#############----issue

# str1="gekeks"
# str2="seeekg"
#
# if(len(str1) != len(str2)):
#     print("String length not equal. Hence can't be Anagram!!!!")
# else:
#     for i in str1:
#         if i not in str2:
#             break
#     else:
#         print("Strings are Anagram")

########## method2 ...lets sort the strings

# str1="geeks"
# str2="seekg"
#
# x=list(str1)
# y=list(str2)
# x.sort()
# y.sort()
# print(x)
# print(y)

# if(len(x) != len(y)):
#     print("String length not equal. Hence can't be Anagram!!!!")
#
# else:
#     for i in range(0,len(x),1):
#         if x[i] != y[i]:
#             print("Strings not Anagram")
#             break
#     else:
#         print("Anagram")


# str1="gekeks"
# str2="seeekg"
#
# if(len(str1) != len(str2)):
#     print("String length not equal. Hence can't be Anagram!!!!")
# else:
#     for i in str1:
#         if i not in str2:
#             break
#     else:
#         print("Strings are Anagram")






