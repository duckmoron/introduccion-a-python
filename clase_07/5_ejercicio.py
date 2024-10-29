"""
Crear un programa que muestre un menú:
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
x. Salir

Cada operación aritmética tendrá su propia función
a) Pedir al usuario 2 números
b) Seleccionar una opción del menú
c) Mostrar el resultado
"""


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return False


def ingresar_numero():
    numero = float(input("Ingrese un número: "))
    return numero


def mostrar_resultado(resultado):
    if resultado is not False:
        print("El resultado es:", resultado)
    else:
        print("No se puede dividir por cero")


def main():
    while True:
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("x. Salir")
        entrada = input("Seleccione una opción: ")
        if entrada == "x":
            break
        elif entrada in ["1", "2", "3", "4"]:
            numero_1 = ingresar_numero()
            numero_2 = ingresar_numero()
            if entrada == "1":
                resultado = sumar(numero_1, numero_2)
            elif entrada == "2":
                resultado = restar(numero_1, numero_2)
            elif entrada == "3":
                resultado = multiplicar(numero_1, numero_2)
            elif entrada == "4":
                resultado = dividir(numero_1, numero_2)
            mostrar_resultado(resultado)


main()
