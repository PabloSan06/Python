from Producto import Producto


class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self.id_orden = Orden.contador_ordenes
        # convertimos los productos a una lista
        self._productos = list(productos)

    def agregar_producto(self, producto):
        self._productos.append(producto)  # para agregar el nuevo producto

    def calcular_total(self):
        total = 0  # variable  temporal para almacenar el total temporal

        for producto in self._productos:
            # precio sin el _ encapsulado ya que para esto hicimos el getter and setter
            total += producto.precio
        return total

    def __str__(self):
        productos_str = ''  # variable temporal tmb
        for producto in self._productos:
            productos_str += producto.__str__() + '|'

        return f'Orden: {self.id_orden}, \n Producto: {productos_str}'


if __name__ == '__main__':  # comprobacion del main
    producto1 = Producto('Remera', 600.00)
    print(producto1)
    producto2 = Producto('Pantalon', 2652.56)
    print(producto2)
    productos1 = [producto1, producto2]  # lista de productos

    # Primer objeto orden pasando la lista de productos
    orden1 = Orden(productos1)
    print(orden1)

    producto3 = Producto('Camisa', 3600.00)
    print(producto3)
    producto4 = Producto('Saco', 2652.56)
    print(producto4)
    productos2 = [producto3, producto4]  # lista de productos
    # Segundo objeto orden pasando la lista de productos
    orden2 = Orden(productos2)
    print(orden2)
