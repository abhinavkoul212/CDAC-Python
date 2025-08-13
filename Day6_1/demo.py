class Demo:
    def __init__(self,first,second):
        self.first=first
        self.__second=second

d= Demo(10,20)
print(d.first)
print(d.__second)