# Ejercicio 3:Función recursiva
# Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas
# Puede ser cualquier valor positivo .


numero = int(input("Dime un num : "))


def imprimir_numeros_recursivos(numero):
    if numero >= 1:  # caso base
        print(numero)
        imprimir_numeros_recursivos(numero-1)  # caso recursivo

    elif numero == 0:
        return
    elif numero <= 0:
        print('el valor es incorrecto')


imprimir_numeros_recursivos(numero)
