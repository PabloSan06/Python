# la lista mantiene un orden que se puede modificar (mutable) ,la tupla mantiene un orden y no se puede modificar (inmutable),set en cambio no tiene orden ni permite duplicados o repetidos este no se puede modificar pero si se puede agregar o eliminar set no mantiene ningun indice es decir es una coleccion sin orden ni indice
# nos permite evitar una lista de datos duplicados

# Tipo set

planetas = {'Marte ', 'Jupiter', 'Venus'}
print(planetas)


# Tipo set longitud de

planetas = {'Marte', 'Jupiter', 'Venus'}
print(len(planetas))


# Revisar si un elemento existe dentro de un set ,se puede usar tmb en tuplas y listas
print('Marte' in planetas)

# Revisar si no esta un elemento  dentro de un set ,se puede usar tmb en tuplas y listas
print('Marte' not in planetas)


# Agregar un elemento

planetas.add('Tierra')  # add es funcion agregar

print(planetas)

# Eliminar elementos ,puede arrojar un error si el elemento no existe

# funcion que ante mal tecleado o inexistencia del elemento da error
planetas.remove('Tierra')

print(planetas)


# Eliminar elementos ,puede arrojar error si el elemento no existe

planetas.discard('Tierra')
print(planetas)

# Eliminar elementos ,puede arrojar error si el elemento no existe

# funcion que ante mal tecleado o inexistencia del elemento no da error simplemente se sigue ejecutando el programa
planetas.discard('tierra')

print(planetas)

# Limpiar set o conjunto

planetas.clear()

print(planetas)

# Eliminar set

del planetas

print(planetas)


# para definir un conjunto
conjunto2 = set()
conjunto1 = {'bye', }
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)

conjunto1.add('hola')
print(conjunto1)

# Preguntamos si  el numero 3 no esta en el conjunto 1
print(3 not in conjunto1)


# como hacer la igualdad de dos conjuntos

print(conjunto1 == conjunto2)  # Nos devuelve como respuesta un booleano


# operaciones en conjunto

conjunto3 = conjunto1 | conjunto2  # la linea une los dos conjuntos
print(conjunto3)


# que elemento tienen en comun y se guardara en el elemento 3
conjunto3 = conjunto1 and conjunto2
print(conjunto3)


# Asigna el valor que esta en el conjunto1 y no en el conjunto2
conjunto3 = conjunto1-conjunto2
print(conjunto3)


# Asigna el valor que esta en el conjunto2 y no en el conjunto1
conjunto3 = conjunto2-conjunto1
print(conjunto3)

# elementos que no comparten o que son diferentes entre ambos
conjunto3 = conjunto1 ^ conjunto2
print(conjunto3)


# dentro del conjunto 3 se estan guardando dos subconjuntos
conjunto3 = conjunto1 | conjunto2

# para saber si el conjunto1 es un subconjunto del conjunto3
print(conjunto2.issubset(conjunto3))

print(conjunto1.issubset(conjunto3))

# si el conjunto 3 esta dentro del conjunto 1
print(conjunto3.issubset(conjunto1))

# si el conjunto 3 esta dentro del conjunto 2
print(conjunto3.issubset(conjunto2))


# Preguntamos si los elementos del conjunto1 estan dentro del 3
print(conjunto3.issuperset(conjunto1))

# si es verdadero quiere decir que el conjunto3 es un superconjunto
print(conjunto3.issuperset(conjunto2))

print(conjunto2.issuperset(conjunto3))

# Como saber si ambos conjuntos son disconexos ,esto es si comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2))  # no hay cosas en comun

# los conjuntos no son totalmente mutables, ni totalmente inmutables
# Convertir un conjunto totalmente en inmutable

# esto lo hace totalmente inmutable , no se puede agregar ,modificar ,ni eliminar elementos del conjunto.
conjunto1 = frozenset
