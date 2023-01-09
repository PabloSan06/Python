# Eje 10 : HAcer programa que pida cadena por teclado ,luego
# meter los caracteres en una lista sin repetir caracteres

cadena = input("Digite una cadena : ")
lista = []
for i in cadena:
    if i not in lista:  # busca si no esta en la lista
        lista.append(i)  # Lo agregamos a la lista

print(f'\Sin repetir ninguno : \n {lista}')
