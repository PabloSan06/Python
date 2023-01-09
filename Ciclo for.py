"""


dias = ["Lunes", "Martes", "Miercoles",
        "Jueves", "Viernes", "Sabado", "Domingo"]


# 1 ejemplo de for en listas
# for x in dias:
# print(x)


# 2 ejemplo de for con break

# for x in dias:
#   print(x)
#  if x == "Viernes":
#     break

# 3 ejemplo de for con exepción
# for x in dias:
#  if x == "Viernes":
#       break
#   print(x)

# 4 ejemplo FOR de repe
#numero = 5
# for x in range(numero):
#    print("Argentina")
# else:
#    print("Campeón")


cal = 0
suma = 0
i = 0

cal1 = 0
calbaja = 11

for i in range(10):
    cal = float(input("Ingrese la nota del alumno : "))
    suma = suma+cal

    if cal <= calbaja:
        calbaja = cal


promedio = suma/cal

print(f"La calificacion mas baja es   {calbaja} ")
print(f"El valor promedio es  {promedio} ")
"""
