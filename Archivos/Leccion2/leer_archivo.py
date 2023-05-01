# con metodo read es el default para leer
# r de read  , es otro modo distinto del write
# letras 'w' escribe     ,'r' lee,'a' genera algo mas sobre lo generado,'x' crea archivo
# t =text , b =binary,w+ escribir y leer info,r+
# si el archivo con el cual trabajariamos no esta en la misma carpeta tendriamos que poner la ruta c: \  \
archivo = open('prueba.txt', 'r',  encoding='utf8')
# print(archivo.read(15))  # le pasamos el total de caracteres,lineas y/o parrafos
# print(archivo.read(79))
# print(archivo.readline())
# print(archivo.readline())


# Vamos a iterar el archivo ,cada una de las líneas con for
# for linea in archivo:
# print(linea)
# print(archivo.readlines()[2])  # con este metodo traigo una lista, utilizo corchete para decir que linea elemento de lista quiero

# anexamos info ,copiamos a otro cuantas veces lo ejecutemos

archivo2 = open('copia.txt', 'a', encoding='utf8')
archivo2.write(archivo.read())
archivo.close()  # cerramos el primer archivo
archivo2.close()  # cerramos el segundo archivo


print('Se ha terminado el proceso de leer y copiar archivos ')
