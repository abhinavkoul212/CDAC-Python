class MyException(Exception):
    def __init__(self,message="Something went wrong"):
        super().__init__(message)
        self.message=message
        #print(self.message)

# a=10
# if a>5:
#     raise MyException(")   #---------------- is not working/printing default message string