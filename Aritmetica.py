
class Aritmetica:
    """
    Docstring
    Vamos a hacer en esta clase operaciones 

    """

    def __init__(self, operandoA, operandoB):  # recibe parametros en metodo inicializador
        self.operandoA = operandoA
        self.operandoB = operandoB
    # Method sumar

    def sumar(self):  # metodo sumar
        return self.operandoA+self.operandoB

    def resta(self):  # metodo resta
        return self.operandoA-self.operandoB

    def producto(self):  # metodo multi
        return self.operandoA*self.operandoB

    def dividir(self):  # metodo div
        return self.operandoA/self.operandoB

# creamos una instancia de la clase aritmetica


# constructor #le pasamos los argumentos para los operandos
aritmetica1 = Aritmetica(7, 9)
print(aritmetica1.sumar())  # llama al metodo sumar


# constructor #le pasamos los argumentos para los operandos
aritmetica2 = Aritmetica(20, 2)
print(aritmetica2.resta())  # llama al metodo sumar


# llama al metodo sumar
print(f'la resta de los num es: {aritmetica1.resta()}')
# llama al metodo sumar
print(f'el producto  de los num es: {aritmetica2.producto()}')
# llama al metodo sumar
print(f'el divi  de los num es: {aritmetica1.dividir():.2f}')
