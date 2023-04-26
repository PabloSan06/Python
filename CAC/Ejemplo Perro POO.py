from time import process_time_ns


class Producto:
    # aca estamos definiendo la abstraccion es decir las caracteristicas de las intancias que generemos
    contandor_instancias = 0
    # se definio los atributos de los productos ,tendra precio y producto
    # los atributos de instancia en py se definen dentro del constructor o inicializador
    # inicializador o constructor =el primer metodo que se ejecuta cuando instancio el objeto
    # ejemplo ;la  primer torta inicializara
    # self es la instancia propia  que estoy generando
    # le defino determinados valores a la instancia
    # en el main ,en el modulo principal
    # print(type())
    # la clase es la declaración

    # para no instanciar siempre le ponemos estos atributos requeridos
    def __init__(self, pNombre, pPrecio):
        # parametronombreNombre(atributo) y parametroPrecio(atributo)
        # pasando dos paramteros al constructor que seran los que voy a asignar a las instancias que genere
        # se le pasa self ya que es el inicializador ,la instancia  se pone como primer parametro ,en java es  this
        # el resto de los parametros pueden ser pasados
        # como todos los metodos **nombre de un parametro de dicc, lista  ,*args,**K cualquier recurso de py,
        Producto.contandor_instancias += 1
        print("Soy un nuevo producto")
        # se inicializa un nuevo producto
        self.nombre = pNombre
        # generar todos los atributos en el init por buenas practicas
        # aca se genera la variable de instancia
        # self.nombre es el atributo de la variable y pNombre es el parametro , valor  que recibo arriba
        # por cada variable que genero le asigno un valor
        # con self llamo a la instancia que estoy generando ,
        # recibiendo c/u  de parametro, asignando al atributo nombre a la  instancia que estoy generando
        # definiendo aca mismo , en el init las variables de instancia
        # todas las intancias tendran este atributo
        # en py no tengo que definir la variable de forma explicita
        self.precio = pPrecio

        # asignando al atributo precio a la  instancia que estoy generando

    def __del__(self):
        # este sera el ultimo metodo que se ejecute dado que el primer metodo es el init cuando se ejecute el programa
        # aca se eliminara el instanciado , en este  producto
        # el espacio de memoria asignado a esa variable es descartado cuando ocurre el del
        # generalmente no lo vamos a utilizar este metodo dado que no eliminara la instancia
        print("No sirve mas")

    def __str__(self):
        return f"Soy el producto {self.nombre} y salgo {self.precio}"


mi_producto = Producto("Zapato", 600)
# el scope de mi producto es desde que se intancia este
print(mi_producto.contandor_instancias)
# instaniamos la clase producto en objetos con comportamiento ,estado e identidad
mi_producto = Producto("Zapatilla", 200)
# inicializando el contador con los atributos self.nombre y self.precio = pPrecio
print(mi_producto.contandor_instancias)
Producto.contandor_instancias = 8
print(mi_producto.contandor_instancias)
print(mi_producto.contandor_instancias)


print(mi_producto)

print(type(mi_producto))  # asignando variables de intancia
print(mi_producto.nombre)  # atributo de instancia mi_producto

mi_producto.nombre = "Zapatilla"
mi_producto.precio = 20

print(mi_producto.nombre)


class Perro:
    # Atributo de Clase
    genero = "Canis"

    def __init__(self, nombre, edad):
        print("Nacio un perrito")
        self.nombre = nombre
        self.edad = edad

    def __del__(self):
        print("He tenido una buena vida..")

    # Método de instancia
    def imprimir(self):
        self.ladrar("Guau")
        return f'{self.nombre} tiene {self.edad} años.'
    # Otro método de instancia

    def ladrar(self, sonido):
        return f'{self.nombre} dice {sonido}.'

    # Se puede reemplazar el método imprimir() con __str__()
    def __str__(self):
        return f'{self.nombre} tiene {self.edad} años.'


miMascota = Perro("Paka", 11)

print(miMascota)


print(miMascota.nombre)
miMascota.imprimir()
miMascota.ladrar("Guau guau!")

print("Género:", miMascota.genero)
print(miMascota.imprimir())
print(miMascota.ladrar("Guau, guau!"))
print(miMascota)

miMascota = None

print("Se terminó el susper sistema")
