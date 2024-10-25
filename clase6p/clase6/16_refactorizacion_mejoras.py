def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(dividendo, divisor):
    if divisor == 0:
        return
    else:
        return dividendo / divisor


def introducir_numeros():
    n1 = int(input("Introduce el primer número: "))
    n2 = int(input("Introduce el segundo número: "))
    return n1, n2


def realizar_operaciones(numero_1, numero_2):
    resultados = []
    funciones = [sumar, restar, multiplicar, dividir]
    for funcion in funciones:
        resultado = funcion(numero_1, numero_2)
        if resultado is not None:
            resultados.append(resultado)
        else:
            resultados.append("No se puede dividir por cero")
    return resultados


def mostrar_resultado(resultados):
    print("Resultados:")
    for resultado in resultados:
        print(resultado)


def main():
    numero_1, numero_2 = introducir_numeros()
    resultados = realizar_operaciones(numero_1, numero_2)
    mostrar_resultado(resultados)


main()
