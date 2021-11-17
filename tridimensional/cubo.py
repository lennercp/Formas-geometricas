from tridimensional.forma3d import Forma3D
from math import *

class Cubo(Forma3D):
    def volume(self, lado):
        return lado ** 3
    
    def diagonal(self, lado):
        return lado * sqrt(3)
