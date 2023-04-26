class Persona:
    contador_personas = 0  # variable de clase#contexto estatico

    @classmethod  # metodo de clase#contexto estatico
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1  # vamos ir incrementando de 1 a 1
        return cls.contador_personas

    def __init__(self, nombre, edad):  # contexto dinamico

        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad
    # en cada instancia una variable de instancia o un atributo de instancia ej nombre se reiniciara en 0 pero eso no va a afectar nunca a variable de clase porque responde a la clase y no al objeto.
    # al no relacionarse directamente con el objeto nunca se reinicia sino que va aumentanto de 1 en 1 y eso le da el valor al id persona

    def __str__(self):
        return f'Persona [{self.id_persona} ={self.nombre} {self.edad}]'


persona1 = Persona('Pablitus', 36)
print(persona1)

persona2 = Persona('Anu', 32)
print(persona2)


persona3 = Persona('Emi', 62)
print(persona3)


# va a llamar al metodo de clase y va  a generar un aumento, osea que el proximo sera el siguiente
Persona.generar_siguiente_valor()
persona4 = Persona('Pablitus', 66)
print(persona4)


print(f'Valor de contador de personas: {Persona.contador_personas} ')
