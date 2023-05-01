"""
En Python, el método __exit__ es un método especial que se utiliza en combinación con la instrucción with para definir un contexto de ejecución. Este método se utiliza en conjunto con el método __enter__ para crear un contexto que se ejecutará cuando se entre en un bloque with, y que se limpiará cuando se salga de dicho bloque.

El método __exit__ se utiliza para liberar los recursos y hacer la limpieza necesaria cuando se sale de un bloque with. Este método toma tres argumentos: exc_type, exc_value y traceback. Estos argumentos contienen información sobre cualquier excepción que haya ocurrido durante la ejecución del bloque with, si es que hay alguna.

La sintaxis general para usar __enter__ y __exit__ juntos en un bloque with es la siguiente:

with objeto as alias:
    # Código dentro del bloque with
    
El método __enter__ se llama al entrar en el bloque with, y el objeto que devuelve se asigna al alias especificado. El método __exit__ se llama cuando se sale del bloque with, y se encarga de la limpieza y la liberación de recursos.

Aquí hay un ejemplo de cómo usar __enter__ y __exit__ para crear un bloque with personalizado que maneja la conexión y desconexión a una base de datos:

En este ejemplo, la clase BaseDeDatos define los métodos __enter__ y __exit__. Al entrar en el bloque with, se llama a __enter__, 
que devuelve una conexión a la base de datos. Cuando se sale del bloque with, se llama a __exit__, que se encarga de desconectar la conexión. De esta forma, el bloque with asegura que la conexión a la base de datos se maneje de manera segura y se libere correctamente.


"""


class BaseDeDatos:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.conexion = None

    def __enter__(self):
        self.conexion = conectar(self.host, self.port)
        return self.conexion

    def __exit__(self, exc_type, exc_value, traceback):
        desconectar(self.conexion)


with BaseDeDatos('localhost', 5432) as conexion:
    # Código dentro del bloque with
