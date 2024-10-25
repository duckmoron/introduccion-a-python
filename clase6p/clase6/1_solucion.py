"""
Crear 4 funciones: sumar, restar, multiplicar y dividir
que impriman el resultado

Crear una lista de funciones
invocarlas con 2 números predeterminados
"""


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
