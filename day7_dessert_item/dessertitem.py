from abc import abstractmethod, ABC


class DessertItem(ABC):

    def __init__(self,name):
        self.name=name

    @abstractmethod
    def costOfItem(self):
        pass
    #concrete method
    def NameOfItem(self):
        return self.name

    def __str__(self):
        pass

