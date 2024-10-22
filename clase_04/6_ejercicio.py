"""
Mejorar el ejercicio de la tabla de multiplicacion, usando isdecimal()
para verificar si el usuario inglesa un numerio entero o negativo
"""

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_nueva = []

while True:
    entrada = input("Ingrese un número y te daré su tabla de multiplicación: ")
    if entrada.isdecimal():
        numero = int(entrada)
        break
    else:
        print("Debes ingresar un número entero.")
        continue

for num in lista:
    multiplicacion = num * numero
    lista_nueva.append(multiplicacion)

print("La lista original es:", lista)
print("La lista nueva es:", lista_nueva)

