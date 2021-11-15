from abc import ABC, abstractmethod

class FormaPlana(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def diagonal(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass