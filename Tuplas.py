
# siguen el orden de los elementos como se agregan pero no se pueden eliminar
# es decir son inmutables a diferencia de las listas que si son mutables
# Formas de utilizar tuplas
#se pueden transformar las listas en tuplas y las tuplas en listas
# adentro de tuplas se puede usar index,count,len
nombres = ("Matias", "Maxi", "Sonia", "Euge")

numeros = (1, 2, 3, 4, 5)
valor = (True, False, True)

mix = ("Rodrigo", 2, 4, True, False)

# print(numeros)

# print(nombres[2])

# print(numeros[1:4])

# Actualizar tupla

# x=list(nombres)
# x[1]="Pablo"
# nombres=tuple(x)

# print(nombres)

# print(nombres[1])

# Desempaquetar tupla

(uno, dos, tres, cuatro, cinco) = numeros
"""
print(uno)

print(dos)

print(tres)

print(cuatro)

print(cinco)
"""

# metodos de una tupla count(),index().

print(numeros.count(5))

print(numeros.index(5))

# definimos una tupla

cocina = ('cuchara', 'cuchillo', 'tenedor')
print(cocina)

# conocer el largo de la tupla

cocina = ('cuchara', 'cuchillo', 'tenedor')
print(len(cocina))


# Acceder a un elemento ,para esto se usa conrchetes no parentesis como todas las tuplas

print(cocina[0])

# mostrar la manera inversa
print(cocina[-1])

# Acceder a un rango

print(cocina[0:1])


# Ejemplo

# esto es un string ,no una tupla ya que no tiene una coma(,) al final
verduras = ('papa')

# recorremos los elementos de una tupla

for cocinar in cocina:  # Print esta usando \n para saltos de linea
    print(cocinar, end='')  # usamos end para eliminar los saltos de linea


cocinaLista = list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print('\n')

# del cocina # esto es para eliminar una tupla

import math #importamos la clase math para hacer uso de la funcion sqrt

#Ejercicio de math

numero=int(input('Digite un num positivo'))

while numero <0:
    print('Error ->debe ser un numero positivo ')
    
    numero=int(input('Digite un numero positivo :'))

print(f'\n su raiz cuadrada es :{math.sqrt(numero):.2f}')#salto de linea y con el .2f solo dos numeros 




# Dada la siguiente tupla

tupla = (13, 1, 8, 3, 2, 5, 8)  # Definimos la tupla

# Crear una lista que solo incluya los numeros menores a 5
# e imprima por consola  [1,3,2]

lista = []

# Filtramos los element menores a 5 de la tupla

for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)

# Repaso Tupla

# puede tener diferentes tipos de datos adentro
tupla = (4, 'Pini', 6.78, [1, 5, 6, 3], 4, 6, 8, 'PAblo')

print(tupla)


print(4 in tupla)#accion booleana ,respuesta de tipo booleana
#lo que podemos usar dentro de tuplas son : index,count,len 
#En tuplas se puede convertir de tupla a lista y de lista a tupla 
 


