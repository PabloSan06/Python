
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
