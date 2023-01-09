# Ejercicio2 :Operaciones de conjuntos con listas

# Escribir un programa que tenga 2 listas y que a continuación
# cree las sig listas (no debe haber repe)
# 1 lista de palabras que aparecen en las listas
# 2 lista de palabras que aparecen en la primer lista , pero no en la segunda
# 3 lista de palabrass que aparece en la segunda lista , pero no en la primera
# 4 lista de palabras que aparecen en ambas listas


lista1 = [1, 2, 3, 4, 5, 6, 2, 4, 5, 2, 3, 51, 2, 3, 4, 6, 67, 4]

lista2 = [2, 3, 5, 6, 6, 85, 51, 3, 4, 3, 2, 3, 4, 6, 4]


# Eliminar los elementos repetidos de ambas listas con conjuntos

conjunto1 = set(lista1)

conjunto2 = set(lista2)


union = list(conjunto1 | conjunto2)  # unimos los dos conjuntos

solo1 = list(conjunto1-conjunto2)  # solo muestra conj 1
solo2 = list(conjunto2-conjunto1)  # solo muestra conj 2
interseccion = list(conjunto1 & conjunto2)  # ambas listas

print(f"lista de palabras que aparecen en las listas :{union}")

print(
    f"lista de palabras que aparecen en la primer lista , pero no en la segunda :{solo1}")
print(
    f"lista de palabrass que aparece en la segunda lista , pero no en la primera  :{solo2}")
print(f"lista de palabras que aparecen en ambas listas  :{interseccion}")
