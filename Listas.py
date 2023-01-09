# Listas en python
# Las listas se conocen en otros lenguajes como arreglos o vectores


nombres = ["Euge", "Sonia", "Matias", "Lucas", "Rodrigo"]
numeros = [1, 2, 3, 4, 5, ]
barios = [1, 5, 4, "Pablo", "juan", True, False, False]

print(barios)
print(len(barios))


# Acceder a elementos de una lista

print(nombres[0:3])


# Cambiar elementos de una lista
barios[5] = False
print(barios)


# Metodos de las listas append(), remove()
barios.append(True)
print(barios)

barios.remove(4)
print(barios)

# Concatenamos lista

lista1 = [1, 2, 1, 3]
lista2 = [4, 5, 6, 1]

lista3 = lista1+lista2

print(lista3)


lista3.extend([7, 8, 9])  # funcion para agregar elementos a la lista

print(lista3)


print(lista3.index(5))  # funcion para saber donde esta ese elemento

# Como saber  cuando hay registros repetidos dentro de una lista

print(lista3.count(1))  # cuenta cuantos valores hay iguales dentro de la lista

# poner nuestra lista al revez

lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos

lista3 = [1, 2, 3]*2
print(lista3)


# Metodos de ordenamiento #ya se vieron el metodo burbuja el de insercion y el de seleccion

lista3.sort()  # ordena ascendente
print(lista3)
lista3.sort(reverse=True)  # ordena descendentemente
print(lista3)


# Pilas usando listas

pila = [1, 2, 3]


# Agregar elementos  a la pila por el final

pila.append(4)
pila.append(5)
print(pila)


# Sacamos elementos desde el final

elementoBorrado = pila.pop()  # Quita el ultimo elemento y lo guarda en la variable

print(f'Sacamos el elemento :{elementoBorrado}')

print(f'La pila ahora queda asi :{pila}')

# Colas con listas
# Estructura de datos de tipo fifo(first input /first output)


cola = ['Pablo', 'Maria', 'Sanguinetti']


# agregamos

cola.append('Jose')
cola.append('Jose')
cola.append('Jose')

print(cola)

# sacamos

seRetira = cola.pop(0)

print(f'Atendido {seRetira}')


print(cola)

seRetira = cola.pop(1)

print(f'Atendido {seRetira}')


print(cola)
