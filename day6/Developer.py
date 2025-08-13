import Employee

class Developer(Employee):

    def writeCode(self):
        print("Dev is writing code")

d= Developer()
print("------------")
d.printEmp()
print("------------")