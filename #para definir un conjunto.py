# para definir un conjunto
conjunto = set()
conjunto1 = {'bye', }
conjunto.add(7)
conjunto.add('Hola')
print(conjunto)

conjunto1.add('hola')
print(conjunto1)

# Preguntamos si  el numero 3 no esta en el conjunto 1
print(3 not in conjunto1)

print(conjunto1 == conjunto)  # Nos devuelve como respuesta un booleano
