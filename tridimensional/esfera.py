from tridimensional.forma3d import Forma3D
from math import *

class Esfera(Forma3D):
    def volume(self, raio):
        return 4/3 * pi * raio**3
    
    def diagonal(self):
        print('Esfera não há diagonal')