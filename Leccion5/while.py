num1 = int(input("ingresa un num "))
while num1 != 0:
    print(num1)
    num1 = int(input("ingrese un num"))
print("fin del ejercicio")


# EJERCICIO: Ingresar 5 valores por teclado, obtener su suma y su promedio.
cont = 1
suma = 0
while cont <= 5:
    num = int(input("Ingrese un número: "))
    suma = suma + num   # Acumulamos, es equivalente suma += num
    cont = cont + 1     # Incrementamos, es equivalente cont += 1

print("La suma es:", suma)
print("El promedio es:", suma/cont)
