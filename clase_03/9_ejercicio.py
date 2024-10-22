"""
Crear una lista del 0 al 5
iterar la lista con for, imprimir cada número
si el número es 3, imprimir un mensaje de alerta
"""

from time import sleep

lista = [0, 1, 2, 3, 4, 5]

for numero in lista:
    sleep(0.5)
    print(numero)
    # if numero == 3:
    if numero == int(input("Número: ")):
        print("¡Alerta! Se ha encontrado el número.")