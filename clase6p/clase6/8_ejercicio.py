"""
A partir del siguiente código, reemplazar los print por return.
Al final, imprimir el resultado de cada función llamando con print.

def sumar(a, b):
    print(a + b)


def restar(a, b):
    print(a - b)


def multiplicar(a, b):
    print(a * b)


def dividir(a, b):
    print(a / b)


funciones = [sumar, restar, multiplicar, dividir]

for funcion in funciones:
    funcion(2, 3)
"""


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(dividendo, divisor):
    if divisor == 0:
        return "No se puede dividir por cero"
    else:
        return dividendo / divisor


funciones = [sumar, restar, multiplicar, dividir]

numero_1 = float(input("Ingrese el primer número: "))
numero_2 = float(input("Ingrese el segundo número: "))

for funcion in funciones:
    print(funcion.__name__)
    resultado = funcion(numero_1, numero_2)
    print(resultado)
