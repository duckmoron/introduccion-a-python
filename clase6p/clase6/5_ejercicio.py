"""
Ejercicio con funciones con parámetros predeterminados
Crear una función dividir que reciba dos parámetros, uno opcional y otro obligatorio,
y devuelva el resultado de la división de ambos. Si se pasa un solo argumento,
dividir / 1.
"""


def dividir(dividendo, divisor=1):
    if divisor == 0:
        print("No se puede dividir por cero")
    else:
        print(dividendo / divisor)


dividir(10)
dividir(10, 2)
dividir(10, 0)  # ZeroDivisionError: division by zero
