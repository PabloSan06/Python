from computadora import Computadora
from monitor import Monitor
from orden import Orden
from raton import Raton
from teclado import Teclado


teclado1 = Teclado('HP', 'USB')
monitor1 = Monitor('HP', '167 pulgadas')
raton1 = Raton('HSKAO', 'wireles')
computadora1 = Computadora('HP', monitor1, teclado1, raton1)


teclado2 = Teclado('Acer', 'USB')
monitor2 = Monitor('Acer', '111 pulgadas')
raton2 = Raton('Acer', 'wireles')
computadora2 = Computadora('HP', monitor2, teclado2, raton2)


teclado3 = Teclado('Gamer', 'USB')
monitor3 = Monitor('Gamer', '167 pulgadas')
raton3 = Raton('Gamer', 'wireles')
computadora3 = Computadora('HP', monitor3, teclado3, raton3)


teclado4 = Teclado('Apple', 'USB')
monitor4 = Monitor('Apple', '111 pulgadas')
raton4 = Raton('Apple', 'wireles')
computadora4 = Computadora('Apple', monitor4, teclado4, raton4)

teclado5 = Teclado('Samsung', 'USB')
monitor5 = Monitor('Samsung', '111 pulgadas')
raton5 = Raton('Samsung', 'wireles')
computadora5 = Computadora('Samsung', monitor5, teclado5, raton5)

computadora6 = Computadora('HP', monitor1, teclado3, raton4)
computadora7 = Computadora('HP', monitor3, teclado3, raton5)


computadoras1 = [computadora1, computadora2, computadora7, computadora4]

orden1 = Orden(computadoras1)
orden1.agregar_computadora(computadora3)

print(orden1)


computadoras2 = [computadora3, computadora5, computadora6]

orden2 = Orden(computadoras2)


print(orden2)
