from abc import ABC, abstractmethod  # importando la clase abstracta y su metodo
# ABC=onvierte una clase en abstracta


class FiguraGeometrica(ABC):  # clase padre figura geometrica
    def __init__(self, ancho, alto):
        if self._validar_valores(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'Valor erroneo para el ancho :{ancho}')
        if self._validar_valores(alto):
            self._alto = alto
        else:
            self.alto = 0
            print(f'Valor erroneo para el alto :{alto}')

    @property  # generamos el get para la variable ancho
    def ancho(self):
        return self._ancho

    @ancho.setter  # generamos el set para la variable ancho#Si sacaramos los setter quedarian como atributos solo de lectura
    def ancho(self, ancho):
        if self._validar_valores(ancho):  # validaciones en el setter
            self._ancho = ancho
        else:
            print(f'Valor erroneo para el ancho :{ancho}')

    @property  # generamos el get para la variable alto
    def alto(self):
        return self._alto

    @alto.setter  # generamos  set para la variable alto
    def alto(self, alto):
        if self._validar_valores(alto):  # validaciones en el setter
            self._alto = alto
        else:
            print(f'Valor erroneo para el alto :{alto}')

    @abstractmethod  # decorador#no se implementa en la clase padre figura geometrica,como no debe implementarse se pone pass
    # va a ser obligatorio para las clases hijas cuadrado y rectangulo que tengan el metodo calcular area
    def calcular_area(self):
        pass

    def __str__(self):
        return f'Figura geometrica [Ancho: {self._ancho}, Alto: {self._alto}]'

    # metodo encapsulado que se debe usar solo en esta clase , solo de manera interna
    def _validar_valores(self, valor):
        return True if 0 < valor < 10 else False  # trabajara de manera encapsulada
