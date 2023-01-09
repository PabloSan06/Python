#Ejercicio 5 :Conver de temperaturas 
#Realizar  2 funciones para convertir de °C a Farenheir y viceversa

#de °C a F

def celsius_fahrenheit(celsius):
    return celsius*9 /5+32 

#de F a °C
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit-32)*5/9

celsius=float(input('Digite el valor de celsius: '))

resultado=celsius_fahrenheit(celsius)

print(f'{celsius}C A F >{resultado:.2f}')



fahrenheit=float(input('Digite el valor de fahrenheit : '))
resultado=fahrenheit_celsius(fahrenheit)
print(f'{fahrenheit} F a C -> {resultado:.2f}')