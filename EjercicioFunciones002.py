# en  py lo que mas se utiliza es kwargs para recibir los argumentos , llave valor
# se pasan tantos parametros independientes como quisieramos
def listarTerminos(**terminos):
    for llave, valor in terminos.items():  # kwargs significa: key word argument
        print(f'{llave}:{valor}')


listarTerminos()  # no recibe nada ,nada se va a mostrar
listarTerminos(IDE='Integrated Develoment Enviroment', PK='Primary Key ')
listarTerminos(Nombre='Lionel Messi', Posicion=10)


def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)


nombres2 = ['Pablo', 'Analia', 'Soledad']

desplegarNombres(nombres2)
desplegarNombres('Carla')
# desplegarNombres(10)#no es un objeto iterable
# con un parentesis adentro se convierte en una tupla iterable ,es decir que se convirtio a tupla para iterar nombre
desplegarNombres((10, 11))
# con corchetes adentro se convierte en una lista iterable ,es decir que se convirtio a tupla para iterar nombre
desplegarNombres([22, 55])

# Funciones Recursivas  (funciones que se llama a si misma para completar una tarea)necesitan un caso base y un caso recursivo,necesitando esto para que no se convierta en un ciclo interminable


def factorial(numero):
    if numero == 1:  # Caso Base
        return 1
    else:
        return numero*factorial(numero-1)  # caso recursivo
numeroFactorial=int(input('Digite el numero para calcular el factorial :'))

resultado = factorial(numeroFactorial)  # Lo hacemos en codigo duro
print(f'El factorial del numero {numeroFactorial} es :{resultado}')
