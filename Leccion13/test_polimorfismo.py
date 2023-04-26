from Empleado import Empleado
from Gerente import Gerente

# metodo con el cual los objetos se logren asociar ,a  apartir de pasar objetos por parametros


def imprimir_detalles(objeto):
    # De manera indirecta llama al str de la clase empleado o de la clase geretne
    # print(objeto)
    print(type(objeto))  # Esto es para saber el tipo de dato que recibe
    print(objeto.mostrar_detalles())
    # metodo is instance para preguntar a un objeto si pertenece a cierta clase ,osea si es una instancia de cierta clase ;
    # aqui comprobamos si la clase objeto es de la clase gerente
    if isinstance(objeto, Gerente):
        print(objeto.departamento)
    # me muestra el objeto departamento =ciencias naturales , ya que si objeto es gerente imprime cs.nat


empleado = Empleado('Ariel', 60000)
imprimir_detalles(empleado)


gerente = Gerente('Pablo', 700000, 'Ciencias Naturales')
imprimir_detalles(gerente)
# ver que nos muestra clase padre empleado y tambien nos muestra clase hijo gerente esto es el polimorfimos , osea multiples formas en tiempo de ejecucion
