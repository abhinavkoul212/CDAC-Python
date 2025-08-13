from abc import ABC, abstractmethod

class DesertItem(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def costOfItem(self):
        pass
    def getName(self):
        return self.name