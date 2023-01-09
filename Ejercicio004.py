# Ejercicio 4:Sumar numeros pares dentro de un rango
# Hacer un programa para sumar números pares dentro
# de un rango ,por ejemplo :
# suma de numeros pares
# suma=240


a = int(input("Digite donde comienza la suma :  "))
b = int(input("Digite donde finaliza  la suma :  "))

suma = 0

for i in range(a, b+1):
    if i % 2 == 0:  # esto es para
        suma += i
print(f"\n La suma de pares dentro de los mumero es :{suma} cochino")
        