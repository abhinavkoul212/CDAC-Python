from abc import abstractmethod, ABC


class DessertItem(ABC):

    def __init__(self,name):
        self.name=name

    @abstractmethod
    def costOfItem(self):
        pass
    #concrete method
    def NameofItem(self):
        return self.name

