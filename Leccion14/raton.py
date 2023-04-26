
from dispositivo_entrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contador_ratones = 0

    def __init__(self, marca, tipo_entrada):
        # llamo  a la clase contador ratonesy luego el operador simplificado de suma
        Raton.contador_ratones += 1
        self._id_raton = Raton.contador_ratones
        # llamar a la herencia de la clase dispositivo entrada #le pasamos loa rgumentos la clase marca y tipo entrada
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'Id: {self._id_raton}, Marca : {self._marca},Tipo entrada:{self._tipo_entrada} '


# Hacemos pruebas

if __name__ == '__main__':  # comprobación sobre la ejecución
    raton1 = Raton('HP', 'USB')  # cracion de objeto de la clase raton
    print(raton1)
    raton2 = Raton('Acer', 'BLuetooth')
    print(raton2)
