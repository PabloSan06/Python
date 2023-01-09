
'''
miVariable =3
print(miVariable)
miVariable= "asjkdansdkjnsajnskjdskdjskd"
print(miVariable)
miVariable=3.5
print(miVariable)
x=10
y=2
z= x + y

print(id(x))

print(id(y))

print(id(z))


a =True

print (type(a))

...
# Tipos int,float,string,bool

x=10
print(x)
print(type(x))
x=14.5
print(x)
print(type(x))
x="LALaaaaaaaauuu"
x=True
print(x)
print(type(x))
x=False
print(x)
print(type(x))


#manejo de caracteres (string)

miBandaFavorita="Jambao"
caracteristicas=  " 4 integrantes"
print("Mi grupo favorito es "+ miBandaFavorita + caracteristicas)

#numero1="7"

#numero2="8"

#print(int(numero1)+int(numero2))

#tipos booleanos (bool)

miBooleano=1>2
print(miBooleano)

if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")


# procesar la entrada del usuario 
# funcion input 

#resultado= input("Digite un numero ") # regresa dato tipo string
#print(resultado)


#Conversion de la entrada de datos 

numero1=int(input("Escribe el primer numero :"))

numero2=int(input("Escribe el segundo numero :"))

resultado=numero1+numero2
print("El resultado de la suma es :", resultado)

'''
#titulo = input("Proporciona el titulo del libro : ")
#autor = input("Proporciona el autor del libro : ")


#print(titulo, "Fue escrito por : ", autor)
"""
operandoA=8
operandoB=5

suma=operandoA+operandoB


#print("El resul es",suma)
print(f'El resul de la suma es: {suma}')



resta =operandoA-operandoB
print(f'El resul de la resta es: {resta}')


multiplicacion=operandoA*operandoB
print(f'El resul de la multi es: {multiplicacion}')

division=operandoA/operandoB
print(f'El resul de la divbi es: {division}')

division=operandoA//operandoB
print(f'El resul de la divbi (int)es: {division}')

modulo=operandoA%operandoB
print(f'El resul de la residuo: {modulo}')

exp=operandoA**operandoB
print(f'El resul de la exp: {exp}')
"""
"""
numero1 = input("Escribe un número: ")
numero2 = input("Escribe el otro número: ")

numero1_como_int = int(numero1)
numero2_como_int = int(numero2)

area=numero1_como_int*numero2_como_int
perimetro=(numero1_como_int*numero2_como_int)*2

print(f'El resul de la area: {area}')
print(f'El resul de la perimetro: {perimetro}')
"""


"""
miVariable3 = 6
print(miVariable3)

# operardores de reasignación

miVariable3 = miVariable3 + 1
print(miVariable3)


miVariable3 += 1
print(miVariable3)


miVariable3 *= 5656551
print(miVariable3)


miVariable3 -= 6000
print(miVariable3)


miVariable3 /= 2
print(miVariable3)
"""

# operadores de comparacion


"""
d = 6

a = 66

resultado = d == a  # Comprobamos si son iguales

print(resultado)


resultado = d != a  # Comprobamos si son distintos

print(resultado)


resultado = d < a  # Comprobamos si d es menor que a

print(resultado)

resultado = d > a  # Comprobamos si d es mayor que a

print(resultado)

resultado = d >= a  # Comprobamos si d es mayor o igual  que a

print(resultado)

resultado = d <= a  # Comprobamos si d es menor o igual  que a

print(resultado)




numero1=int(input("Escribe el primer numero :"))

"""
"""
a = int(input("Escribe el primer numero :"))


print(f"deses el residuo de la div es : { a%2 }")

if a * 2 == 60:

    print(f"El numero {a:} multiplicado por 2  es sesenta  ")


else:

    print(f"El numero {a:} multiplicado por 2 no es sesenta  ")


a = int(input("Escribe tu edad  :"))

edad_adult = 18

print(f"deses el residuo de la div es : { a%2 }")

if a > edad_adult:

    print(f"Sos mayor de  {a:} edad  ")


else:

    print(f"Sos menor de  {a:} edad  ")
    
    
    
"""

"""
a = int(input("Escribe el primer numero :"))

b = int(input("Escribe el segundo numero :"))

print(f"deses el residuo de la div es : { a%2 }")

if a * 2 and a*3 >= 10:

    print(f"El numero {a:} y el {b:}  son mayores a 6  ")


else:

    print(f"El numero {a:}  y el  {b:}  son menores que 6  ")



"""
"""
# operador and


j = True


K = False

resultado = j and K
print(resultado)


# operador or
j = True


K = False

resultado = j or K
print(resultado)


# operador not


j = True


K = True

resultado = not K
print(resultado)


a = int(input("Escribe un numero :"))


if a >= 0 and a <= 5:

    print(f"El numero {a:} esta entre 0 y 5  ")


else:

    print(f"El numero {a:} no esta entre 0 y 5 ")


print("Saluditos")



"""
"""
# operador or

vac = False
diadesc = False


if vac or diadesc:

    print("Tenes vacas ")


else:

    print("No Tenes vacas")


print("Saluditos")
"""

"""
a = int(input("Dime tu edad  :"))

if a >= 20 and a <= 30:

    print(f"Tu edad , {a:} años esta 20 y 30 años ")



else:

    print(f"Tu edad , {a:} años no esta 20 y 30 años ")


print("Saluditos")
"""
"""
a = int(input("Dime un numero   :"))
b = int(input("Dime otro numero   :"))

if a > b and a != b:

    print(f"El primer numero es mayor {a} ")

elif b > a and b != a:
    print(f"El segundo numero es mayor {b} ")

else:
    print("Segui participando  ")
    
    
"""

a = (input("Dime el nombre del libro:"))
b = int(input("Dime el ID numerico del libro :"))
c = int(input("Dime el precio  del libro :"))
d = (input("Indicar si es gratuito o no (True/False):"))

if d == 'True':
    d = True
elif d == 'False':
    d = False
else:
    d = "El valor es incorrecto ,debe escribir alguna opción correcto , osea True/False"

print(f'''
      El libro {f"El nombre del libro es {a}"}
      
      del ID {f"El nombre del libro es {b}"}
      
      el precio es (f"El nombre del libro es {c}")
      
      y la gratituidad es {d}
      
     ''')
