class Persona:  # Creamos una clase #Clase es la plantilla ,atributos son características y objetos son acciones

    # los parametros son las variables que van recibiendo y modificando los atributos  # metodo especial method init dunder#palabra de referencia que es la variable self,como operador
    def __init__(self, nombre, apellido,edad,*args,**kwargs ):#la palabra self es identica a this en java,se le puede cambiar el nombre ,siempre llevando el primer lugar
        # self como operador apunta a los atributos  # a la izq es atributo a la derecha esta la variable,self siembre dentro de los metodos
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.args=args
        self.wkargs=kwargs #argumento variables del tipo diccionario
    #py no posee mod de acceso ,como java private , publi 
    def mostrar_detalle(self):
        print(f'La clase Persona tiene los siguientes datos :{self.nombre}{self.apellido}{self.edad},la dire es :{self.args},los datos importantes son :{self.wkargs} ')

persona1 = Persona('Pablo', 'Sanguinetti', 32)



persona1.mostrar_detalle()