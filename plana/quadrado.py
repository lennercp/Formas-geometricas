from plana.formaPlana import FormaPlana
from math import *

class Quadrado(FormaPlana):
    def area(self,lado):
        return lado * lado

    def diagonal(self,area):
        return area * sqrt(2)

    def perimetro(self,lado):
        return lado * 4