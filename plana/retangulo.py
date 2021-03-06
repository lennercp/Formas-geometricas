from plana.formaPlana import FormaPlana
from math import *

class Retangulo(FormaPlana):
    def area(self,lado1, lado2):
        return lado1 * lado2

    def diagonal(self, lado1, lado2):
        return sqrt(lado1 ** 2 + lado2 ** 2)

    def perimetro(self, lado1, lado2):
        return lado1 * 2 + lado2 * 2
