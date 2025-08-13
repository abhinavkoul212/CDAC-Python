class Employee:

    def __init__(self):
        self.empId = 1
        self.name="Abc"


    def hello(self):
        print("Hello from Emp")

class Dev(Employee):
    # pass
    def hello(self):
        print("Hello from DEV")

class Test(Employee):
    # pass
    def hello(self):
         print("Hello from Test")

e= Employee()
e.hello()

d=Dev()
d.hello()

t= Test()
t.hello()


class DevTest(Test,Dev):

    def hello(self):
        super().hello()
        print("This is from DevTest")



dt= DevTest()
dt.hello()