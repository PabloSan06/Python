seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 millones', 'Posicion': 'Extremo derecho'},
    11: {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 millones', 'Posicion': 'Extremo derecho'},
    24: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 millones', 'Posicion': 'Media Punta'},
    19: {'Nombre': 'Nicolas Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 millones', 'Posicion': 'Defensa Central'},
    1: {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 millones', 'Posicion': 'Portero'},
    1: {'Nombre': 'Emiliano Martinez', 'Edad': 29, 'Altura': 1.95, 'Precio': '22 millones', 'Posicion': 'Portero'},
    21: {'Nombre': 'Angel Correa', 'Edad': 27, 'Altura': 1.71, 'Precio': '45 millones', 'Posicion': 'Delantero'},
    5: {'Nombre': 'Leandro Paredes', 'Edad': 28, 'Altura': 1.80, 'Precio': '15 millones', 'Posicion': 'Centrocampista'},
    6: {'Nombre': 'German Pezzella', 'Edad': 31, 'Altura': 1.86, 'Precio': '5 millones', 'Posicion': 'Defensa'},

}


#for llave, valor in seleccionArgentina.items():
   # print(llave, valor)


#otra forma de recorrer el diccionario 
for i in seleccionArgentina:
    print(f'{i}->{seleccionArgentina[i]}')