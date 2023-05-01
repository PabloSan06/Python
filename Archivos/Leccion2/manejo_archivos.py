# Declaramos una variable

# estamos indicando que si esta archivo no existe lo vamos a crear de lo contrario nuestro metodo open va a buscar nuestro archivo
try:
    # con el encoding utf8 permite poner los acentos
    # si una vez que hice el write para seguir agregando hay que poner a sino se pisa
    archivo = open('prueba.txt', 'w', encoding='utf8')
    archivo.write(
        'Programamos con diferentes tipos de archivos ,ahora en txt \n')
    archivo.write('Los acentos son importantes para las palabras \n')
    archivo.write('Ejemplo :acción , ejecución y producción  \n')
    archivo.write('Dale booooooooooooocaaaaaaa \n')
    archivo.write('Cons esto terminamos ,ahora en txt \n')
    archivo.write('Quedo piola \n')
    archivo.write('Saludos')
except Exception as e:
    print(e)

finally:  # siempre se ejecuta
    archivo.close()  # Con esto se debe cerrar el archivo
# metodo open , para abrir archivo que ya existe o abrir un archivo que no exista ,lo crea de forma automatica
# se le puede indicar varios parametros para leer info de un archivo ol escribir info hacia un archivo
# la  w es de write
