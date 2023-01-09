"""
# Ciclo While (mientras o durante )

condi = True

while condi:
    print("Ejecu")

else:
    print("Fin ciclo")


"""
"""

contador = 0
while contador < 4:
    print("Es cuatrochi")
    contador += 1

else:
    print("Fin de ciclo")
"""
"""

cont = 0

while cont < 3:
    print("Boca campeon ", cont)
    cont += 1
else:
    print("Finde   ")
"""
"""
min=1
cont=5
while cont >=min :
    print(cont)
    cont -=1

"""
# Ciclo for
"""

cadena = "Hola"
for letra in cadena:
    print(letra)

else:
    print("Fin del ciclo For ")
"""

"""
for letra in "Alemania":
    if letra == "a":
        print(f"La letra encontrada fue {letra} ")

else:
    print("Fin del for ")
"""
"""
for letra in "Alemania":
    if letra == "a":
        print(f"La letra encontrada fue {letra} ")
        break
else:
    print("Fin del for ")
""""""
from os import name
for i in range(6):
    if i % 2 == 0:
        print(f"Valor {i} ")

for i in range (6):
    if i% 2 !=0  :
        continue
    print(f"Valor {i} ")
"""
"""

año = int(input("Ingrese el año por favor "))
tipo_a = None

if año % 4 == 0 and año % 100 != 0:

    tipo_a = "Bisiesto"

elif año % 100 == 0 and año % 400 == 0:

    tipo_a = "Bisiesto"
else:

    tipo_a = "No Bisiesto"


print(f'El año {año} es {tipo_a} ')

"""
"""
contador = 0
suma = 0
numero = 1

while numero != 0:
    numero = int(input("Digite un numero entero y 0 para terminar :    "))

    suma += numero
    contador += 1

if contador == 0:

    print("No dijito ningun num")

else:
    print(f"la suma total es {suma}")
    
"""
"""
n = int(input("Ingrese la cantidad de datos a ciclar    "))

if n > 0:
    positivos = 0
    negativos = 0
    nulos = 0

    for i in range(n):
        dato = int(input("Ingrese numero  "))

        if dato > 0:
            positivos += 1

        elif dato < 0:
            negativos += 1
        else:
            nulos += 1

    print("\nLos + fueron ", positivos,
          "\nLos - fueron ", negativos,

          "\nLos nulos fueron ", nulos)

else:
    print("Dijite los num necesarios")

"""
"""

cal = 0
suma = 0
i = 0

cal1 = 0
calbaja = 11

for i in range(10):
    cal = float(input("Ingrese la nota del alumno : "))
    suma = suma+cal

    if cal <= calbaja:
        calbaja = cal


promedio = suma/cal

print(f"La calificacion mas baja es   {calbaja} ")
print(f"El valor promedio es  {promedio} ")

"""

"""


"""
# Repe de numeros
numero = 1
# while numero <= 10:
#    print(numero)
#    numero += 1

# Repe de num con break

# while numero <= 10:
#    print(numero)

#    if numero == 6:
#        break
#    numero += 1

# Repe de numero con continue

# while numero<10 :
#      numero+=1
#     if numero ==6 :
#         continue
#     print(numero)

# suma de naturales

numeros = int(input("introduce un num natural:"))

resul = 3

control = 2

while control <= numeros:
    resul += control
    control += 1

print("La suma de numeros Naturales es ", resul)

