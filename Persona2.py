"""
#El objetivo del encapsulamiento es que no se pueda acceder de forma directa a los atributos de la clase

#Metodo set = establecer ,colocar,nos permite modificar los atributos de una clase 

#metodo get =obtener ,nos permite obtener los atributos de una clase 
#Para cada atributo requerimos de un metodo set y uno getter


"""


class Persona2:

    def __init__(self, nombre, apellido, edad):  # metodo inicializador para los atributos
        self._nombre = nombre  # atributos encapsulados
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalle(self):
        print(
            f'Los datos a mostrar son los siguientes :{self._nombre} {self._apellido} {self._edad}'' años')

    @property  # esto es un decorador#nos permite acceder de forma indirecta dado que no requiere ser llamado el parametro
    def nombre(self):  # Metodo Getter
        print('estamos usando el metodo get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  # Metodo Setter
        print('estamos usando el metodo set')
        self._nombre = nombre

    @property  # esto es un decorador#nos permite acceder de forma indirecta dado que no requiere ser llamado el parametro
    def apellido(self):  # Metodo Getter
        print('estamos usando el metodo get')
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):  # Metodo Setter
        print('estamos usando el metodo set')
        self._apellido = apellido

    @property  # esto es un decorador#nos permite acceder de forma indirecta dado que no requiere ser llamado el parametro
    def edad(self):  # Metodo Getter
        print('estamos usando el metodo get')
        return self._edad

    # @edad.setter
    # def edad(self,edad):#Metodo Setter
    #     print('estamos usando el metodo set')
    #     self._edad=edad


persona1 = Persona2('Pablo', 'Sanguinetti', '32')
# persona1._nombre esto no se utiliza asi dado que esta oculto el atributo

# asi llamamos al metodo getter , en el cual no es necesario enviar parametro
print(persona1.nombre, persona1.apellido, persona1.edad)


persona1.nombre = 'Pablo Maria'  # esta utilizando metodo set para moficicarlo

print(persona1.nombre)  # muestra el metodo get aqui para obtener y mostrarlo

print(persona1.mostrar_detalle())  # llamamos al metodo mostrar detalles

# Atributo read-only sería la edad porque no tiene el metodo set
print(persona1.edad)
