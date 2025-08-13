from day7.customexceptons import MyException
class Employee:

    def __init__(self,empId,name,salary):
        self.empId = empId
        self.name=name
        #self.salary = salary
        try:
            self.salary = salary
            raise MyException("since salary ws not in integer type hence setting it to default 10k")
        except MyException as e:
            print("in except block")
            self.salary = 10000
            print(e)
            # print("since salary ws not in integer type hance setting it to default 10k")
        finally:
            # self.salary = 10000
            # self.HRA = self.salary * 0.5
            self.HRA = self.salary * 0.5
            self.PT = 200
            self.PF = (10000/100)*12

    def grossSal(self):
        print(self.salary+self.HRA+ self.PF+self.PT)
         #return (self.salary+self.HRA+ self.PF+self.PT)

    def netSal(self):
        return (self.grossSal() - self.PF -self.PT)

    # def __gt__(self, other):
    #     if self.empId > other.empId:
    #         return True
    #     else:
    #         return False
    #
    # def __lt__(self, other):
    #     if self.empId < other.empId:
    #         return True
    #     else:
    #         return False


    def printEmp(self):
        print("Employee ID:", self.empId)
        print("Employee Name:", self.name)
        print("Employee Gross Salary:", self.grossSal())
        print("Employee NetSalary:", self.netSal())

e1=Employee(1,"Abhinav","Akhilesh")
e1.grossSal()


