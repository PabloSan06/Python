# Ejerccio 11 :Agenda tel

# diccio donde clave sera el nombre del usuario y el valor

# 1.New contact
# 2.Borrar contacto
# 3.Ver contacts
# 4.Salir


agenda = {}

while True:

    print('\t.:Menú:.')
    print('1.New Con')
    print('2.Delete contac')
    print('3.Ver contactos existentes')
    print('4.Salir')

    opcion = int(input('Digite una opcion del menu'))

    if opcion == 1:
        nombre = input('Digite el nombre del contacto : ')
        telefono = nombre = input('Digite el numero del tel :')

        if nombre not in agenda:
            agenda[nombre] = telefono
            print('Contacto agregado')

        else:

            print('Ya existe ese contacto ')

    elif opcion == 2:
        nombre = input('Cual es el name del contacto ')
        if nombre in agenda:
            del (agenda[nombre])
            print('Se ha eliminado el contacto requerido')

        else:
            print('Este contact no existe en la agenda ')

    elif opcion == 3:
        print('Agenda de contactos ')
        for clave, valor in agenda.items():
            print(f'Nombre:{clave},telefono:{valor}')
    elif opcion == 4:
        print('Gracias por utilizar ')
        break

    else:
        print('Opcion que no existe ingresaste ')

    # list unpacking

    def show(name, lastName):
        print(name+''+lastName)

    person = ["Pablo", "Sanguinetti"]

    # Pasamos uno por uno los datos de la lista funcion
    show(person[0], person[1])

    show(*person)  # Esto es lo mismo que lo anterior pero le pasamos todo junto

    # desempaquetamos a travez de una tupla
    person2 = ("Pablo ", "Sanguinetti ")

    show(*person2)

    person3 = {"lastName": "Lucero", "name": "NAty"}
    show(**person3)

    numbers = [1, 2, 3, 4, 5]

    for n in numbers:
        print(n)

    else:
        print('esto ya fue ')

    # List comprehension

    names = ["Pablo", "Marta", "Antonio", "Anu"]
    # Esto regresa una nueva lista#sin modificar las listas,tupla ,diccionarios, arrys o lo que este recorriendo
    alongP = [p for p in names if p[0] == 'P']

    print(alongP)

    bit = [{"name": "Pablo", "country": "Arg"},
           {"name": "Pedro", "country": "Bol"},
           {"name": "Jose", "country": "Ger"},
           ]
    Arg = [b for b in bit if b["country"] == "Arg"]

    print(Arg)
    print(bit)

    # Paso de argumentos (funciones)

    def mi_funcion2(name, lastName):
        print("Hola chicos")
        print(f'Nombre:{name},Apellido:{lastName}')

    mi_funcion2('Maria', 'Sangui')
    mi_funcion2('Noe', 'Lopez')
    mi_funcion2('Carla', 'Vazquez')


# return en funciones

def sumar(a, b):

    return a + b
# resultado=sumar(78,22)

#print(f'El resultado de la suma es {resultado}')


print(f'el resultado de la suma es : { sumar(22,45)}')


def sumar2(a, b):
    return a + b


resultado = sumar2()
print(f'Resul de la suma :{resultado}')

print(f'Resul de la suma :{sumar2(22,434)}')

# argumentos ,variables en funciones ,cuando no sabemos que cantidad de argumentos va a recibir


# *args =va a recibir argumentos variables , por eso se pone este parametro
def listarNombres(*nombres):

    for nombre in nombres:  # se va a convertir en una tupla
        print(nombre)


listarNombres('Charlie', 'Pablitus', 'Pablingo', 'Luisa')
listarNombres('Pabli', 'Pablitus', 'Pablingo', 'Pablis')


