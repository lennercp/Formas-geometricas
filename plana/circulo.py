from plana.formaPlana import FormaPlana
from math import *

class Circulo(FormaPlana):
    def area(self, raio):
        return pi * raio ** 2

    def perimetro(self, raio):
        return 2 * pi * raio

    def diagonal(self):
        print("Círculo não tem diagonal")