# Ejercicio 01:Crear funcion para sumar los valores recibidos de tipo numericos
# Utilizanco argumentos variables *arg como parametro de la funcion y agregar como resultado la suma de todos los valores pasados como argumentos .


# definimos una funcion

def sumar_valor(*args):  # recibimos cantidad de  parametros indefinidos

    resultado = 0

    # iteramos el elemento

    for valor in args:
        resultado += valor
    return resultado
# Llamammos a la funcion


print(sumar_valor(3, 5, 9, 2, 342323423))
