from Empleado import Empleado

# gerente es la clase hija de empleado


class Gerente(Empleado):  # union de empleado a gerente a partir de la herencia
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento

    def __str__(self):
        return f'Gerente [Departamento: {self.departamento}] {super().__str__()}'
