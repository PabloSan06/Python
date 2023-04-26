class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other):  # si o si requiere sobreescribir para sumar objetos de add
        return f'{self.nombre}  {other.nombre}'

    def __sub__(self, otro):  # resta
        return self.edad - otro.edad


persona1 = Persona('Pablitus', 66)
persona2 = Persona('Anitus', 96)


# persona1.__add__(persona2)  sintaxis interna y automatica


# aqui sucederia la sintaxis interna y automatica, llamando el primer objeto al metodo dunder add y dentro pasa el otro objeto
print(persona1+persona2)


print(persona1-persona2)
