# ejercicio 9 :mostrar una frase sin espacios y contar su long
# hacer un programa donde el usuario ingrese una frase   ,se le
# devolvera la misma frase pero sin espacios en balnco , ademas un contador sin espacios en blanco


frase1 = input("Digite una frase :")

frase2 = " "

for i in frase1:
    if i != " ":
        frase2 += i

frase1 = frase2


print(f'\n frase final :{frase1}')

print(f'N° de caracteres :{len(frase1)}')
