class Producto:
    contador_productos = 0  # variable de clase

    def __init__(self, nombre, precio):
        Producto.contador_productos += 1  # Aumento para la variable de clase
        # Asignación desde la variable de clase
        self._id_producto = Producto.contador_productos
        self._nombre = nombre
        self._precio = precio

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    # Sobreescribimos el metodo str
    def __str__(self):
        return f'Id Producto:{self._id_producto},Nombre:{self._nombre},Precio:{self._precio}'


if __name__ == ' main ':  # Solo sera visible si la prueba se ejecuta desde aqui
    producto1 = Producto('Remera', 600.00)
    producto2 = Producto('Pantalon', 2652.56)
