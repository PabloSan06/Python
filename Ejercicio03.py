# Ejercicio 3 :Insertar elementos y ordenarlos
# Pedir números y meterlos en una lista ,cuando el usuario
# introduzca un numero 0 , nuestro programa dejaria de insertar.
# Por ultimo ,nmostrar los números de menor a mayor


lista = []
salir = False


while not salir:
    numero = int(input('Digite un numero: '))

    if numero == 0:
        salir = True
    else:
        lista.append(numero)

lista.sort()  # La lista esta ordenada con esta función


print(f'\n Lista ordenada :\n{lista}')
