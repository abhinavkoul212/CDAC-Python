from employee import Employee
class MarketingExe(Employee):

    Gross_sal= 0

    def __init__(self, empId, name, salary):
        super().__init__(empId, name, salary)
        self.phoneAll=1500
        self.travelAll=10000

    def grossSal(self):
        return super().grossSal() +self.phoneAll+self.travelAll

