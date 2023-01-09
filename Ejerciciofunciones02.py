# Ejercicio 2:Funcion con *args para multiplicar
# Crear una función para multiplicar los valores recibidos
# de tipo numerico ,utilizando argumentos variables * args
# como parametro de la función y regresar como resultado
# la multiplicacion de todos los valores pasados como argumentos


# Definimos la función para multiplicar

def multiplicar_valores(*numeros):  # el mas utilizado es *args
    resultado = 1  # El cero no nos ayuda a multiplicar
    for numero in numeros:
        resultado *= numero

    return resultado

# Llamamos a la funcion


print(multiplicar_valores(3, 5, 15, 25, 3456))  # Le pasamos los argumentos
