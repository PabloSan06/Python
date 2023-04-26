
from Orden import Orden
from Producto import Producto


producto1 = Producto('Remera', 600.00)
producto2 = Producto('Pantalon', 2652.56)
producto3 = Producto('Camisa', 3600.00)
producto4 = Producto('Saco', 2652.56)
producto5 = Producto('Sandalias', 152.56)
producto6 = Producto('Blusa', 358)


productos1 = [producto1, producto2]  # lista de productos
# Primer objeto orden pasando la lista de productos
orden1 = Orden(productos1)
orden1.agregar_producto(producto3)
orden1.agregar_producto(producto4)
print(orden1)

print(f'Total de la orden 1: {orden1.calcular_total()} ')
productos2 = [producto5, producto6]  # lista de productos
# Segundo objeto orden pasando la lista de productos
orden2 = Orden(productos2)
orden1.agregar_producto(producto1)
orden1.agregar_producto(producto2)
print(orden2)
print(f'Total de la orden 2: {orden2.calcular_total()} ')
