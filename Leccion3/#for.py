# for
# a diferencia del while el for es exacto
'''
ciclos exactos=while/for
Ciclos inexactos=while
'''
# Range va a generar una serie de valores entre un valor inicial ,un valor final y el incremento
# Esta es una sintaxis para Py , dista bastante de js o java
# tenemos un valor inicial ,un fin y un salto/incremento
# El valor final en el range no es inclusivo
# para recorrer listas etc


for cont in range(1, 10, 1):  # inicio#fin#salto

    print(cont)


cajon_frutas = ["pepino", "puerro", "zanahoria", "ajo", "lechuga"]  # lista

for fruta in cajon_frutas:
    # print("La fruta es ", fruta)

    pago = int(input("Pagame :"))
    if pago > 0:
        print("Toma la fruta es ", fruta)
    else:
        print("Sali de aca rata ")


# Lista de numeros
numeros = [1, 2, 3, 4, 5]

for num in numeros:
    print(num)


# Ejemplo con valor ingresado por usuario

N = int(input("Ingrese el valor maximo del contador: "))


for cont in range(1, N+1, 1):  # inicio,fin,salto/inc

    print(cont)

# Suma numeros
suma = 0
num = int(input("Ingrese un nume "))

while num != 0:  # se corta el while con 0
    sum += num  # suma=suma+num
    # se velve a pedir para evitar caer en ciclo infinito
    num = int(input("decime un numero :"))

print("la suma de los ingresados es :", suma)


for numero in range(0, 11, 1):
    print(numero)
    if numero == 10:
        print("aguante el diego")


else:  # el else del for
    print("Cerro la verdu")
