#clase=plantilla , atributos = caracteristicas,metodos = comportamiento

class Persona:  # Creamos una clase #Clase es la plantilla ,atributos son características y objetos son acciones

    # los parametros son las variables que van recibiendo y modificando los atributos  # metodo especial method init dunder#palabra de referencia que es la variable self,como operador
    # la palabra self es identica a this en java,se le puede cambiar el nombre ,siempre llevando el primer lugar
    def __init__(self, nombre, apellido,dni,edad,  *args, **kwargs):
        # self como operador apunta a los atributos  # a la izq es atributo a la derecha esta la variable,self siembre dentro de los metodos
        # *args =argumentos variables para tuplas
        # *kwargs=argumentos variables para diccionarios
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni  # se encapsula con _ de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs
    # py no posee mod de acceso ,como java private , publi

    # self es igual a this en otros lenguajes #genero otro metodo#self para acceder a los atributos de esa misma clase
    def mostrar_detalle(self):
        print(
            f'La clase Persona tiene los siguientes datos :{self.nombre}el apellido {self.apellido} {self._dni}y {self.edad}años, la dire es : {self.args} ,los datos importantes son :{self.kwargs} ')


# persona1 es un objeto #un constructor Persona  # Se envian argumentos
persona1 = Persona('Pablo', 'Sanguinetti',33914046, 32)
# los objetos no comparten los valores ,solo comparten los atributos
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)

# 1)instanciamos un objeto con argumentos#otro objeto ,persona2 , con un constructor Persona y le paso argumentos
# transformamos la variable en un objeto
persona2 = Persona('Analia', 'Vazquez',32323659, 79)
print(
    f'El objeto 2 de la clase persona 2 :{persona2.nombre},{persona2.apellido},su edad es {persona2.edad}')


# 2)accedemos a esos atributos #otro objeto ,persona2 , con un constructor persona y le paso argumentos
# cuando trabajamos fuera de la clase ,al salir de
persona1 = Persona('Pablo', 'Sanguinetti',33636656, 32)
print(
    f'El objeto 1 de la clase persona 1 :{persona1.nombre},{persona1.apellido},su edad es {persona1.edad}')


persona1.nombre = 'Pablito'

persona1.apellido = 'Elsangui'

persona1.edad = 22

print(
    f'El objeto 1 de la clase persona 1 modificado es :{persona1.nombre},{persona1.apellido},su edad es {persona1.edad}')


# Los atributos son caracteristicas
# los metodos son :el comportamiento que van a tener los objetos
# metodo = función se diferencia el metodo esta asociado a una class y la función no (propia de si misma)

# utilizamos la variable convertida en objeto y a traves del .se accede a los metodos y atributos
persona1.mostrar_detalle()
persona2.mostrar_detalle()  # La referencia en este caso se pasa de manera automatica


# Persona.mostrar_detalle(persona1)#esto ya no se utiliza asi ya #cuando se hace directamente con la clase  ,sin usar  al objeto mara llamar a un metodo si o si una referencia como un objeto)


# carga atributos a objetos sin que esten en el metodo init ,atributo superficial solo esta para pers1
persona1.telefono = '34230948984938098'
print(f'Este es el tel de {persona1.nombre}  {persona1.telefono}')


# print(persona2.telefono) esto no se puede hacer dado que no fue declarado el atributo telefono ,da error

persona3 = Persona('Sanguinitutuis', 'Pablitus',26565923, 32, 'Celular', '01152570133', 'Aristobulo del chave',
                   124123, 'Manzana', 46, 'Casa', 18, Altura=1.85, Peso=10323, colorfavorito='Azul', modelo=2022)
# los que saldran con parentesis sera tupla y con corchetes sera diccionarios
persona3.mostrar_detalle()

#print(persona3._dni)#esto en realidad esta mal dado que estaria sugerido encapsulado.

