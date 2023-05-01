from ManejoArchivos import ManejoArchivos

# manejo de contexto with para no utilizar el finally de forma tal que no lo requiere
# sintaxis simplificada :abre y cierra el archivo
# with open('prueba.txt', 'r', encoding='utf8') as archivo:
# print(archivo.read())

# No hace falta ni el try , ni el finally
# en el contexto de with lo que se ejecuta de manera automatica
# utiliza diferentes métodos : __enter__ primer metodo siendo este donde se abre el archivo
# el siguiente metodo es el que cierra : __exit__
# sin embargo nosotros podemos programar los propios metodos

# la clase ManejoArchivos enlazada hacia variable llamada archivo que accedemos mediante metodo read
# con with llama al metodo por eso sale  obtenemos el recurso
with ManejoArchivos('prueba.txt')as archivo:
    # regresa el nombre del objeto y lo guardamos en la variable archivo
    # varible que esta apuntando al objeto archivo que se abrio y leerlo
    print(archivo.read())  # el metodo exit viene solo al llamar al metodo with
