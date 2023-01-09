#en las listas vemos que se respeta el orden de como se carga porque permite agregar o eliminar los elementos 
#es decir las listas son mutables   
# Lista = Pablo , Pedro , Maria , Emilia


nombres = ['Pablo', 'Pedro', 'Anu', 'Marta', 'Agustina']
print(nombres)
print(nombres[2])

print(nombres[1])


print(nombres[-1])

print(nombres[-2])

print(nombres[0:2])  # ir del inicio de la lista hasta el 2 sin incluirlo


print(nombres[:3])  # desde el indice indicado   hasta el 3


print(nombres[1:])  # desde el indice 1 hasta el final

nombres[3] = 'Cahrlse'
nombres[0] = 'Fredy'
print(nombres)

# iterar una lista

for nombre in nombres:  # nombre es singular ,la lista es plural
    print(nombre)

else:
    print('Se acabaron los element of list ')

# preguntamos cuantos elementos tiene

print(len(nombres))  # le pasamos como parametro la lista

# Agregamos un elemento
nombres.append('Marcelo')
nombres.append([1,2,3])
nombres.append(True)
nombres.append(10.45)
nombres.append(4,5)
nombres.append(6)
print(nombres)

# Insertar un elemento en un indice especifico
nombres.insert(1, 'Alberto')
print(nombres)
nombres.insert(3, 'Debora')
print(nombres)

# Eliminar un elemento

nombres.remove('Pedro')
print(nombres)

# Eliminar el ultimo elemento
nombres.pop()

print(nombres)

# Eliminar un elemento especifico

del nombres[2]  # del significa delete especifico
print(nombres)

# Eliminar,borrar o limpiar  todos los elementos
nombres.clear()
print(nombres)

# Eliminar la lista
#del nombres
# print(nombres)
