from FiguraGeometrica import FiguraGeometrica
from Color import Color


# cuadrado hereda de dos padres color y fig geometrica
class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        # en herencia multiple no se usa super para evocar a padre ,ya que no sabriamos a cual evocaria
        # en herencia multiple se llama directo a la clase padre
        # super.__init__(lado)
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.alto*self.ancho

    def __str__(self):
        return f'{ FiguraGeometrica.__str__(self)} {Color.__str__(self)}'
