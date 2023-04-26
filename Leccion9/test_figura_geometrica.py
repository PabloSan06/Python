from Cuadrado import Cuadrado
from Rectangulo import Rectangulo


print('Creacion de objeto clase cuadrado'.center(50, '_'))
cuadrado1 = Cuadrado(8, 'Azul')

# no toma estas reasignaciones ya que tiene validaciones encapsuladas _validar_valores
cuadrado1.alto = 7
cuadrado1.ancho = 7
# print(cuadrado1.ancho)
# print(cuadrado1.alto)

print(f'Cálculo del área del cuadrado: {cuadrado1.calcular_area()}')


# MRO =Method Resolution Order, nos va a dar la info del orden en que se va a ejecutar segun jerarquia de clases

# print(Cuadrado.mro())


print(cuadrado1)

print(f'Cálculo del área del rectangulo'.center(50, '_'))
rectangulo1 = Rectangulo(3, 9, 'verde')
# no toma estas reasignaciones ya que tiene validaciones encapsuladas _validar_valores
rectangulo1.ancho = 8

print(f'Calculo del area del rectangulo : {rectangulo1.calcular_area()}')

print(rectangulo1)


# figura1= FiguraGeometrica() No se puede instancia porque es abstracta

print(Cuadrado.mro())
