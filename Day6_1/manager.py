from employee import Employee

class Manager(Employee):

     def __init__(self,empId,name,salary):
          super().__init__(empId,name,salary)
          self.foodAll = (salary/100)*10
          self.managerAll = (salary/100)*5
          self.otherAll = (salary/100)*3

     def grossSal(self):
          return super().grossSal() + self.foodAll+self.managerAll+self.otherAll


