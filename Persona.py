class Persona: # Creamos una clase #Clase es la plantilla ,atributos son características y objetos son acciones 
    
    def __init__(self):  #metodo especial method init dunder #el contrustor esta oculto
        self.nombre='Juan' 
        self.apellido='Vazquez'
        self.edad= 22
        
persona1=Persona()        #este es un constructor ,apuntando directamente al metodo 
print (persona1.nombre)
print (persona1.apellido)
print (persona1.edad)