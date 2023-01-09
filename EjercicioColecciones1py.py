# Ejercicio 1: Eliminar duplicados de una lista

# Escriba un programa donde tenga una lista y que a continuacion
# elimine los elementos repetidos,y mostrar la lista .

# Creamos lista

lista = [1, 6, 7, 8, 6, 8, 8, "Pablo", 5, 7, 43, 66666, 34, 43, "NAtaL"]

# conjunto = set(lista) #elimina los repetidos mediante un conjunto /set
# print(conjunto)

# lista=list(conjunto)#reconvertimos el conjunto a lista

# La conversión hecha en una sola linea de codigo (eficiente)
lista = list(set(lista))
print(lista)
