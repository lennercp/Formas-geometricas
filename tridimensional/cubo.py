from tridimensional.forma3d import Forma3D
from math import *

class Cubo(Forma3D):
    def volume(self, aresta):
        return aresta ** 3
    
    def diagonal(self, aresta):
        return aresta * sqrt(3)
