
"""
# Estacion del año

mes = int(input("Digite un mes del año (1-12 ): "))

estacion = None

if mes == 1 or mes == 2 or mes == 3:
    estacion = "verano"

elif mes == 4 or mes == 5 or mes == 6:
    estacion = "otoño"

elif mes == 7 or mes == 8 or mes == 9:
    estacion = "invierno"

elif mes == 10 or mes == 11 or mes == 12:
    estacion = "primavera"


else:
    estacion = "Error ,no hay num para este mes "

print(f'Para el mes {mes} la estacion es {estacion}')

"""
"""
edad = int(input("Digite su edad: "))

mensaje = None

if 0 <= edad < 10:  # sintaxis simplificada
    mensaje = "La infancia es increible y bella "

elif 10 <= edad < 20:
    mensaje = "Tienes muchos cambios,mucho por estudiar "

elif 20 <= edad < 30:
    mensaje = "Amor y comienza el trabajo "

else:
    estacion = "Error ,netapa de life no reco"

print(f'Tu edad es {edad} , {mensaje}')


"""
"""
# Sistema de calificaciones


cal = int(input("Digite numero de 0 a 10 : "))


if 9 <= cal <= 10:
    print("A")

elif 8 <= cal <= 9:
    print("B")

elif 6 <= cal <= 7:
    print("C")

elif 5 <= cal <= 6:
    print("D")

elif 5 <= cal <= 6:
    print("E")

else:

    print("le pifiaste con el valor")

"""
"""

nam = "Argen"
bar = "Tina"


if nam == "Argen" and bar == "Tina":

    print("Messi y sus amigos")

else:
    print("ahora si ")

"""
"""
num = int(input("Digame un numero"))

if num > 0:
    print("tu numero es positivo y ")
    if num % 2 == 0:
        print("tambien es par ")
    else:
        print("tambien es impar")
else:
    print("Tu numero es negativo")
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
var1 = int(input("Ingresar de la  variable: "))


if var1 >= 0 and var1 <= 5:
    (f"El número ingresado {var1} si esta dentro el rango 0-5")
else:
    print(f"El número que ingreso {var1} no esta en rango ")


var1 = int(input("Dime la edad : "))


if var1 > 20 and var1 < 30 or var1 != 20 and var1 != 30:
    print(f"La edad ingresada  {var1}  esta dentro el rango 20-30")
else:
    print(f"La edad ingresada {var1} esta fuera del rango 20-30 ")
"""

"""
def http_error(status):
    match status:
        case 400:
            return "Solicitud no encontrada"
        case 404:
            return "No encontrado"
        case 418:
            return "Soy una tetera"
        case _:
            return "Se cayo internet"


print(http_error)
"""
"""
num = int(input("Ingrese un numero mayor a 0 para obtener su factorial"))

factorial = 1

if num > 0:
    for n in range(1, (num+1)):
        factorial = factorial*n

    print(f"el factorial del nuemro ,es {factorial} ")
else:
    print("Deci un positivo")
"""

n = 1
par_cont = impar_cont = 0
sumPar = 0
sumImPar = 0

while n != 0:
    n = int(input("Ingrese un numero para test de pares e impares y cero para salir"))
    if n > 0:
        if n % 2 == 0:
            par_cont += 1
            sumPar += n
        else:
            impar_cont += 1
            sumImPar += n
            prom_impar = sumImPar/impar_cont

print("El total de nuemeros impares es ", impar_cont)
print("El total de nuemeros pares es ", par_cont)
print("El total de nuemeros pares es ", sumPar)
print("El total de nuemeros impares es ", sumImPar)
print("El promedio de los impares es  ", prom_impar)


