class MiClase:
    # Variable de clase,este atributo dará a cada objeto el mismo valor
    # dentro del contexto estatico que esta asociada a la clase
    variable_clase = 'Esta es una variable de clase '

    def __init__(self, variable_instancia):  # La variable de,instancia , da diferentes valores
        # a partir del metodo thunder init podemos crear los objetos#contexto dinamico porque se usa para instancia de objeto
        self.variable_instancia = variable_instancia

    @staticmethod  # decorador que modifica metodo para asociarlo a la clase y no al objeto
    def metodo_estatico():  # no recibe la palabra self ya que no accede al dinamico,tampoco puede acceder a los atributos

        # accedimos a travez de la variable de clase ,hasta no haber creado un objeto no podemos acceder a la variable de clase
        print(MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls):  # un metodo de clase recibe un contexto de clase a diferencia del metodo estatico#cls es una referencia a la clase en si mismo puede tener mas parametros y se trabaja a la instacia como se trabaja co self
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)


# accedimos a travez del objeto #los objetos tambien pueden acceder a la variable de clase
miClase1 = MiClase('Esta es una variable de instancia')

print(miClase1.variable_instancia)
print(MiClase.variable_clase)

# accedimos  a travez del objeto #los objetos tambien pueden acceder a la variable de clase
miClase2 = MiClase('Esta es otra prueba de variable de instancia')
print(miClase2.variable_instancia)
print(miClase2.variable_clase)

# se pueden asociar las variables de clase , como en py todas las class y tipos de datos son objetos en cualquier momento podemos asociar una nueva variable a la clase

# al crearlo fuera del cuerpo de la clase,no s edefinio como parte de la plantilla por eso no me permitio de forma auto a la variable de clase2
MiClase.variable_clase2 = 'Valor de variable de clase 2'
print(MiClase.variable_clase2)  # desde la clase misma
print(miClase1.variable_clase2)  # desde los objetos
print(miClase2.variable_clase2)

# Los metodos estaticos se asocian a la clase
MiClase.metodo_estatico()  # metodo estatico dentro del contexto estatico
# el metodo estatico no recibe ninguna info de la clase
# el contexto estatico trabaja desde la clase y el contexto dinamico no puede acceder al estatico hasta que se instancie ,mientras no este el objeto creado se puede seguir tabjando en el estatico pero no el dinamico hasta que cree un objeto.

MiClase.metodo_clase()

# estatico no recibe info de clase en si misma , por eso se dice que no es ta relacionado con la clase se puede sustituir con otro metodo como funcion
# asociar de manera logica que no tenga nada que ver con nuestros atributos #asociar el tipo de metodo que no tenga que trabajar con variables de instancia directamente relacionada con la clase

# decorador para definir metodo de clase

# el metodo estatico sirve para asociar de manera logica algún otro metodo que no tenga nada que ver con los atributos de nuestra clase
# al crear un objeto creamos tambien el contexto dinamico
miObjeto1 = MiClase('variable de instancia')

# las clases de contexto estatico no pueden acceder al dinamico
miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()
