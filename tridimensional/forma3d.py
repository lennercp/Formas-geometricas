from abc import ABC, abstractmethod

class Forma3D(ABC):
    @abstractmethod
    def volume(self):
        pass

    @abstractmethod
    def diagonal(self):
        pass