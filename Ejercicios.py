
# Ejercicio 1 :Iterar un rango de 0 a 10 e imprimir números divisibles entre 3
# Ejemplo de ejecucion :0,3,6,9
# Cargo el indice hasta 11 ya que requiero que me traiga hasta 10
print('Rango de 0 a 10 con numeros divisibles entre 3 ')
for i in range(11):
    if i % 3 == 0:
        print(i)

# Ejercicio 2 :Crear un rango de numeros de 2 a 6 imprimirlos
# ejemplo de ejecucion :2,4,6

print('Rango con valores de inicio =2 y final =6 ')
rango = range(2, 7)
for i in rango:
    print(i)


# Ejercicio 3 :Crear un rango de 3 a 10 pero con incrementos de 2 en 2 en lugar de 1 en 1

# ejemplo de ejecucion :3,5,7,9

print('Rango con valores de inicio =3 ,fin=10 ,incremento=2')
for i in range(3, 11, 2):
    print(i)
