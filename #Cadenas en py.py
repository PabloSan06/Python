# Cadenas en py

nombre = "Pablo {}"

edad=35

nombres = """
Maria
Juan
Pedro
Marcos
Francisco
"""


# trabajar con una cadena

# for x in nombre:
# print(x)

# print(len(nombre))

# print((nombre)*3)

# cortar cadenas

print(nombre[2])

# cadenas y sus metodos:upper (),lower(),replace(),format()

print(nombre.upper())
print(nombres.lower())
print(nombre.replace("a", "3"))

print(nombres.format(edad))

