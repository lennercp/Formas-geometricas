from tridimensional.forma3d import Forma3D
from math import *

class Cubo(Forma3D):
    def volume(self, lado):
        return lado ** 3
    
    def diagonal(self, area):
        return area * sqrt(3)