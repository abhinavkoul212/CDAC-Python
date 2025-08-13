import numpy

a = numpy.array([1, 2, 3, 4, 5,'j'])
print(a)
#ndarray is a multidimensional array object defined in the numpy library. It is used to store and manipulate data in the form of arrays.

#eg: to remember sort a list would fail for not similar data types
#hence for same type elements in array  and also to support element to element  ops. use nd array

for i in a:
    print(type(i))

#reverse the array
print(a[::-1])

#slicing
print(a[1:4])

#append
a = numpy.append(a, [6, 7, 8])
print(a)

#insert
a = numpy.insert(a, 4, [9, 10, 11])
print(a)

#delete
a = numpy.delete(a, [4, 5])
print(a)

#concatenate
b = numpy.array([12, 13, "sunny", 15])
a = numpy.concatenate((a, b))
print(a)

#reshape: means to change the shape of an array
# a = numpy.reshape(a, (2, 7))
# print(a)

a = numpy.delete(a,[6,12])
#print odd and even elements in a
print(a)
for i in a:
    if int(i)%2==0:
        print("Even:",i)
    else:
        print("Odd:",i)




#type of array
print(type(a))

l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]

print(l1 + l2)

c = numpy.array([1, 2, 3, 4, 5])
d = numpy.array([6, 7, 8, 9, 10])
print(c+d)
print(c-d)
print(c*d)
print(c/d)
print(c**d)
print(c%d)
print(c//d)


c = numpy.array([1, 2, 3, 4])
d = numpy.array([6, 7, 8,10])

#Matrix multiplication
print(numpy.dot(c, d))
#Vector multiplication
print(numpy.vdot(c, d))

#copy: deep copy: changes in one array will not affect the other
e = numpy.copy(c)
print(e)

#view: shallow copy: changes in one array will affect the other
f = c.view()
print(f)

#multiple dimensions
g = numpy.array([[1, 2, 3], [4, 5, 6]])
print(g)

#String operations
h = numpy.array(['a', 'b', 'c', 'd'])
i= numpy.array(['e', 'f', 'g', 'h'])
#print(h)
#print(h.dtype)
print(h+i)

j = numpy.array(["I", "am", "a", "student"])
k = numpy.array(["I", "am", "a", "teacher"])
print(j+k)

#split: splits the array into multiple arrays of equal size or as specified by the user
l = numpy.array_split(j, 2)
j1 = numpy.array([1, 2, 3, 4, 5, 6, 7, 8])
l1 = numpy.array_split(j1, 2)
l6 = numpy.array_split(j1, 6)
l8 = numpy.array_split(j1, 8)
l10 = numpy.array_split(j1, 10)
# z1=ny.array.split(g1,2)
print(l)
print(l1)
print(l6)
print(l8)
print(l10)

#Random numbers in numpy
m = numpy.random.randint(100)
print(m)
#Print random number 25 times in a list
n = numpy.random.randint(100, size=(5))
print(n)
n = numpy.random.randint(100, size=(5))
print(n)
n = numpy.random.randint(100, size=(5))
print(n)

#Random numbers in numpy
o = numpy.random.rand()
print(o)
o = numpy.random.rand()
print(o)
o = numpy.random.rand()
print(o)

#Random numbers selected from a list
p = numpy.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(p)
p = numpy.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(p)
p = numpy.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(p)
p = numpy.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(p)

#Shuffle the list: Randomly shuffle the elements of a list
q = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
numpy.random.shuffle(q)
print(q)

#Zeroes: Create an array of zeros
r = numpy.zeros(5)
print(r)

#Ones: Create an array of ones
s = numpy.ones(5)
print(s)

print(s*5)

#Identity matrix: Create an identity matrix
t = numpy.identity(5)
print(t)

#Transpose: Transpose of a matrix
u = numpy.array([[1, 2, 3], [4, 5, 6]])
print(u)
print(u.T)


numpy.




