class Employee:

    def  __init__(self,empId,name,salary):
        self.empId=empId
        self.name=name
        self.salary=salary

    def __repr__(self):
        return "EmpID:"+ str(self.empId) +  "Name: " +str(self.name) + "Salary :" + str(self.salary)

    def __gt__(self, other):
        if self.salary > other.salary:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.salary < other.salary:
            return True
        else:
            return False

    # def __add__(self, other):
    #     return self.salary + other.salary


e1= Employee(10,"Djinkya",50000)
e2= Employee(5,"Akhilesh",20000)
#e3= Employee(4,"Akhilesh",50000)

# list1=[e1,e2]

# print(list1)




list1=[e1,e2]
list1.sort(key=lambda x: x.name) #-----look into this once
print(list1)

#sorted(list1)  #...... method cal is resolved based on the order of EmpIdlets check it its not sorting-------------pending
#print(list1)



