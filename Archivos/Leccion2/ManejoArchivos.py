# METODO ENTER  Y EXIT CONTEXT MANAGER
class ManejoArchivos:  # puedo acceder a manejo de bd a partir de una condición  con esta y clase y metodos
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        print('Obtenemos el recurso '.center(50, '-'))
        # Encapsulamos el codigo dentro del metodo
        self.nombre = open(self.nombre, 'r', encoding='utf8')
        return self.nombre

    # podemos definir el tipo y su valor de excepcion  #traza_error=traceback #metodo para cerrar
    # metodo exit
    def __exit__(self, tipo_exeption, valor_exception, traza_error):
        # con traceback listo todo el texto del error o lista de errores
        # para ver cuando se ejecuta
        print('cerramos el recurso'.center(50, '-'))
        if self.nombre:  # si es verdadero , es decir si esta direccionado a un objeto
            self.nombre.close()  # cerramos el archivo
