from Persona2 import Persona2 

print('Creación de objetos'.center(50,'-'))

if __name__== '__main__':#comprobacion de metodo principal en ejecución.

    persona5=Persona2('Lionel','Messi',34)
    persona5.mostrar_detalle()


    print(__name__)
    
print('Eliminación de objetos '.center(50,'-'))
del persona5  #se ejecuta metodo destructor