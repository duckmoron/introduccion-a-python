"""
EJERCICIO
A partir de
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
- pedir al usuario que ingrese un número 
- multiplicar cada elemento por el número ingresado por usuario
- Guardar el resultado en una nueva lista
- Mostrar la lista original
- Mostrar la nueva lista
"""
# nueva_lista = [elemento * numero for elemento in lista]

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_nueva = []

numero = int(input("Ingrese un número y te daré su tabla de multiplicación: "))

for num in lista:
    multiplicacion = num * numero
    lista_nueva.append(multiplicacion)

print("La lista original es:", lista)
print("La lista nueva es:", lista_nueva)
