class Employee:

    # empId = 1
    # ename = "ram"
    # salary = 100000

    # def __init__(self):
    #     self.empId = 1
    #     self.ename = "Ram"
    #     self.salary = 500000

    def __init__(self, empId="1",ename="Ram", salary=100000):
        self.empId = empId
        self.ename = ename
        self.salary = salary

    def printEmp(self):
        # empId = 75
        print(self.empId)
        # print(empId)
        print(self.ename)
        print(self.salary)

    @staticmethod
    def hello():
        print("Hello from static method")

e: Employee=Employee()
e.printEmp()
e1=Employee(77)
e1.printEmp()
e2=Employee(55,"Shyam",2378497934)
e2.printEmp()
e3=Employee(ename="ruehhfr")
e3.printEmp()

Employee.hello()

class Developer(Employee):
    def __init__(self, empId, ename, salary):
        super().__init__(empId,ename,salary)
        self.developerAllowance=salary*0.05

    def printEmp(self):
        super().printEmp()
        print("Allowance =" ,self.developerAllowance)

    def writeCode(self):
        print("Dev is writing code")

# d= Developer()
# print("------------")
# d.printEmp()
# print("------------")

d1= Developer(22,"abc",1282393)
print("------------")
d1.printEmp()
print("------------")