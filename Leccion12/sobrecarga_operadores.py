"""
Sobrecarga de operador significa que un mismo operador puede comportarse de diferentes formas
ejemplo : la suma se puede comportar de distintas maneras si esta trabajando con tipo string ,enteros o tipos listas.
Entonces dependiendo del tipo con el que estemos trabajando , es el tipo de resultado que vamos a obtener 
Se puede hacer lo mismo pero en clases .Siendo todos herencia de la clase Object , esta siendo la padre de todas.
Debiendo sobreescribir .
Sobrecarga obedece a comportamientos distintos dependiendo de los operandos que se trabaja y la sobreescritura tiene que ver con la herencia a partir de la clase padre (object) 
Operador aritmetico                     magic method

+                                       __add__(self,other)
-                                       __sub__(self,other)
*                                       __mul__(self,other)
/                                       __truediv__(self,other)
//                                      __floordiv__(self,other)
%                                       __mod__(self,other)
**                                      __pow__(self,other)

Operador comparación (logico )  

<                                       __lt__(self,other)
>                                       __gt__(self,other)
<=                                      __le__(self,other)
>=                                      __ge__(self,other)
==                                      __eq__(self,other)
!=                                      __ne__(self,other)



       
    
"""

a = 'buendia'

b = 'casa'

print(a+b)


a = 16

b = 46

print(a+b)


a = [3, 4, 5, 6]

b = [7, 8, 9, 10]

print(a+b)

#miObjeto1+miObjeto2=esto no se puede hacer dado que requiere de una sobrecarga del metodo heredad asociado al operador de suma

