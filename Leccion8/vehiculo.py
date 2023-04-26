class Vehiculo:
    '''
    Definir una clase padre llamada vehiculo y dos clases hijas llamadas
    auto y bicicleta , las cuales heredan de la clase padre vehiculo .
    La clase padre debe tener los siguientes atributos y metodos :


    Vehiculo (clase padre )
    -Atributos (color,ruedas)
    # el metodo thunder init recibe parametros (atributos de clase padre)color y ruedas , metodo thunder str
    -Metodos (__init__(color,ruedas) y __str__() )

    Auto (clase hija de vehiculo)
    -Atributos (velocidad (km/hr ))
    -Metodos (__init__(color,ruedas,velocidad) y __str__())

    Bicicleta (clase hija de vehiculo)
    -Atributos (tipo (urbana/montaña/etc..))
    -Métodos (__init__(color,ruedas,tipo) y __str__())

    Crear un objeto de cada clase

    '''

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return 'Color: ' + self.color + ' , Ruedas:' + str(self.ruedas)


class Auto(Vehiculo):  # la clase empleado es hija y hereda de la clase persona
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__() + ', Velocidad(km/hr): ' + str(self.velocidad)


class Bicicleta(Vehiculo):  # la clase empleado es hija y hereda de la clase persona
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ', Tipo: '+self.tipo


# Primer objeto de  clase padre vehiculo

vehiculo = Vehiculo('Azul', 4)
print(vehiculo)


# Segundo Objeto ,pero ahora para el clase Auto
auto = Auto('Amarello',  4, 124324)
print(auto)


# Tercer objeto , clase bicicleta

bici = Bicicleta('Rojo',  6, 'Montaña')
print(bici)
