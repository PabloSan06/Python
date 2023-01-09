# Diccionarios en python,puede modificarse sus valores.
# Coleccion de datos organizados con una llave y un valor
# nombres = {1: "santi", 2: "alejandro",
#           3: "sonia", 4: True, 5: False, 6: "maxi"}
#tupla = {"nombre": "mdza", "edad": 25, "tup": ("UTN", 2, 4, "pablo")}
#lista = {"nombre": "mdza", "edad": 25, "list": ["UTN", 2, 4, "maria"]}

# print(len(nombres))
# print(len(tupla))
# print(len(lista))

"""
# Acceder a elementos keys(), values(), items().

print(nombres[2])

x = nombres[2]
print(x)

print(nombres.keys())
print(nombres.values())
print(nombres.items())


# Cambiar elementos update().

nombres[3] = "Sanguinetti"
print(nombres)

#nombres.update({3: "carla"})
print(nombres)

# Agregar elemento.

nombres.update({7: "Agrono"})
print(nombres)

"""


# Elimninar elemento pop(), popitem(), del, clear()
# nombres.pop(3)
# print(nombres)

# nombres.popitem()
# print(nombres)

# nombres.clear()
# print(nombres)

#del nombres[2]
# print(nombres)


# dict(key,value)

diccionario = {

    'IDE': 'Integrated Development Envirionment  ',
    'POO': 'Programación Orientada a Objetos',
    'SABD': 'Sistema de administracion de bases de datos ',


}

# verificar cantidad de elementos
print(diccionario)

print(len(diccionario))


# acceder a diccionario con la llave (key)


print(diccionario['IDE'])

# otra forma de recuperar elemento

print(diccionario.get('POO'))

print(diccionario.get('SABD'))

# Modificar los elementos

diccionario['IDE'] = 'Boca Juniors'
print(diccionario)


# como recorrer los elementos

for termino in diccionario:  # Recorremos solo mostrando las llaves
    print(termino)

# Necesitamos una funcion para recorrer un diccionario que muestre la llave y el valor
for termino, valor in diccionario.items():
    print(termino, valor)


# otras maneras de acceder a un diccionario

for termino in diccionario.keys():
    print(termino)  # Muestra solo las llaves


# otro ciclo

for valor in diccionario.values():  # accedemos solo al valor
    print(valor)

# comprobar existenmcia de algun elemento
print('IDE' in diccionario)


# Agregar elemento

diccionario['PK'] = 'Primary Key'

print(diccionario)

# Eliminar un elemento

diccionario.pop('SABD')

print(diccionario)

# Vaciar un diccionario

diccionario.clear()

print(diccionario)

# Eliminar diccionario

del diccionario  # El diccionario se borro


#repaso de diccionario 

diccionarioNuevo={'Azul':'Blue','Rojo':'Red','Green':'Verde','Yellow':'Amarillo'}
print(diccionarioNuevo)

#como eliminar el elemento azul
del(diccionarioNuevo['Azul'])
print(diccionarioNuevo)

#los diccionarios pueden almacenar diferentes tipos de datos 
diccionario2={'Pablo':{'edad':34,'Altura':1.83},'Osvaldo':[45,1.85], 'Emilia':[35,1.78] }
print(diccionario2)