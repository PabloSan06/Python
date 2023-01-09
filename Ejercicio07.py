# Ejercicio 7: Juego adivina el número

# Realizar un juego para adivinar un número . Para ello se debe
# generar un número  aleatorio entre 1 -100 , y luego ir pidiendo
# numeros indicando "es mayor " o "es menor " según sea mayor o menor
# con respecto a N.El proceso termina cuando el usuario acierta
# y allí se debe mostrar el número de intentos .

import random
print("\t.:Juego adivina NumMMMMMMM:. ")
# Toma de 0 a 100 literal ,generamos un numero aleatorio
aleatorio = random.randint(0, 100)

contador = 0
while True:
    numero = int(input("Digite un número: "))
    contador += 1
    if numero > aleatorio:
        print("\t No es el numero ,digite un número menor ")

    elif numero < aleatorio:
        print("\t  No es el número digite un numero mayor ")
    else:
        print(f"Encontraste el num {aleatorio} guampa ")

        break  # Rompe el ciclo y el bucle

print(f"\n Numero de intentos {contador}")
