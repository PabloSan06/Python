class Persona:  # Esta clase hereda de la clase object
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __str__(self):  # Override=sobreescribir los atributos # viene de la clase 0bject#el metodo en una clase padre lo volvemo a definir en clase hijo , asi definimos el comportamiento
        return f'Persona: [Nombre :{self._nombre},Edad:{self._edad}]'


class Empleado(Persona):  # la clase empleado es hija y hereda de la clase persona
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self._sueldo = sueldo

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    def __str__(self):
        # el str de la clase hija y sobreescribiendo con el str de la clase padre
        return f'Empleado: [ Sueldo: {self._sueldo}]{super().__str__()}'


empleado1 = Empleado('JOse', 12, 25909)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)


empleado2 = Empleado('Pablis', 75, 76767)
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)

empleado2.nombre = 'Krakovia'
empleado2.edad = 17
empleado2.sueldo = 89898
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)
