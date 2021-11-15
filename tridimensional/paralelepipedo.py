from tridimensional.forma3d import Forma3D
from math import *

class Paralelepipedo(Forma3D):
    def volume(self, lado1, lado2, lado3):
        return lado1 * lado2 * lado3
    
    def diagonal(self, lado1, lado2, lado3):
        return sqrt(lado1**2 + lado2**2 + lado3**2)
