


# Sentencia if/else
"""
condicion = False

if condicion:
    print("condi verdadera ")


else :

   print("Condi falsa")
"""
"""
# Sentencia if/else

condicion = False

if condicion == True:
    print("condi verdadera ")

elif condicion == False:
    print("condi falsea ")

else:

    print("Condi no dice ninguna condi ")
"""
# Conversion de num a Text

num = int(input("Digite un numero del 1 al 4"))
numTexto = ""

if num == 1:
    numTexto = "Numero uno "

elif num == 2:
    numTexto = "Numero dos "

elif num == 3:
    numTexto = "Numero tres "

else:
    numTexto = "Ingresaste numero erroneo"


print(f'El numero ingresado es {num}- {numTexto}')
