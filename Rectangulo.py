"""

Fig_Geo1=Rectangulo

"""

class FigGeo:

    def __init__(self, ladoA, ladoB):  # recibe atributos en metodo inicializador
        self.ladoA = ladoA
        self.ladoB = ladoB
        
        
    def area(self):  # metodo multiplicar
        return self.ladoA*self.ladoB
    
    


ladoA=int(input('Dime la base '))
ladoB=int(input('Dime la h '))


Fig_Geo1 = FigGeo(ladoA,ladoB)#instanciamos  un objeto de la class rectangulo ,pasandole los dos argumentos 



print(f'La sup de la figura es : {Fig_Geo1.area()}')


