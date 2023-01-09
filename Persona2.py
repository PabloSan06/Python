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

    @property  # esto es un decorador # nos permite acceder de forma indirecta dado que no requiere ser llamado el parametro
    def nombre(self):  # Metodo Getter
        print('estamos usando el metodo get')
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  # Metodo Setter
        print('estamos usando el metodo set')
        self._nombre = nombre

    @property  # esto es un decorador # nos permite acceder de forma indirecta dado que no requiere ser llamado el parametro
    def apellido(self):  # Metodo Getter
        print('estamos usando el metodo get')
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):  # Metodo Setter
        print('estamos usando el metodo set')
        self._apellido = apellido

    @property  # esto es un decorador # nos permite acceder de forma indirecta dado que no requiere ser llamado el parametro
    def edad(self):  # Metodo Getter
        print('estamos usando el metodo get')
        return self._edad

    @edad.setter
    def edad(self, edad):  # Metodo Setter
        print('estamos usando el metodo set')
        self._edad = edad

    def __del__(self):
        print(f'Persona2 :{self._nombre} {self._apellido}{self._edad}')

    # @edad.setter
    # def edad(self,edad):#Metodo Setter
    # print('estamos usando el metodo set')
    # self._edad=edad


if __name__ == '__main__':

    persona1 = Persona2('Pablo', 'Sanguinetti', '32')
    # persona1._nombre esto no se utiliza asi dado que esta oculto el atributo

    # asi llamamos al metodo getter , ya que  no es necesario enviar parametro
    print(persona1.nombre, persona1.apellido, persona1.edad)

    persona1.nombre = 'Juan PEdro'  # esta utilizando metodo set para moficicarlo

    # muestra el metodo get aqui para obtener y mostrarlo
    print(persona1.nombre)

    print(persona1.mostrar_detalle())  # llamamos al metodo mostrar detalles

    # Atributo read-only sería la edad porque no tiene el metodo set dado que esta comentado
    print(persona1.edad)

    # Tarea crear tres objetos mas utilizados los metodos getter and setter
    # para modificar  , y mostrar los cambios

    # Objeto 1 de la tarea
    persona2 = Persona2('Pabli', 'Santis', 66)
    print(persona2.nombre)  # aca se trabaja con get
    print(persona2.apellido)  # aca se trabaja con get
    print(persona2.edad)  # aca se trabaja con get
    persona2.nombre = 'Pablitus'  # aca se trabaja con set
    persona2.apellido = 'Hijitus'  # aca se trabaja con set
    persona2.edad = 88  # aca se trabaja con set
    # con este metodo realizara los cambios que hizo
    print(persona2.mostrar_detalle())

    # Objeto 2 de la tarea
    persona3 = Persona2('Chichi', 'Carnival', 16)
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    persona3.nombre = 'Sancho'
    persona3.apellido = 'Saliquelo'
    persona3.edad = 68

    print(persona3.mostrar_detalle())

    # Objeto 3 de la tarea
    persona4 = Persona2('Elma', 'Cloti', 666)
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    persona4.nombre = 'Fidela'
    persona4.apellido = 'Ofelitis'
    persona4.edad = 44
    print(persona4.mostrar_detalle())

    # si lo llego a importar en otro clase , me va  a advertir hasta donde trae
    print(__name__)
