"""


Fig_Geo1=Cubo

"""


class FigGeo:

    def __init__(self, ladoA, ladoB, ladoC):  # recibe parametros en metodo inicializador
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def cubo(self):  # metodo calcular volumen
        return self.ladoA*self.ladoB*self.ladoC


ladoA = int(input('Dime un ancho '))
ladoB = int(input('Dime el largo'))
ladoC = int(input('Dime la profundidad '))

# instanciamos  un objeto de la class rectangulo pasandole los dos argumentos
Fig_Geo1 = FigGeo(ladoA, ladoB, ladoC)


print(f'El volumen  de la figura es : {Fig_Geo1.cubo()}')
