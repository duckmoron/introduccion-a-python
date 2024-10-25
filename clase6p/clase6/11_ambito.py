BIENVENIDA = "OPERACION"


def sumar(a, b):
    print(BIENVENIDA)
    mensaje = "Sumando..."  # variable de ámbito local
    print(mensaje)
    return a + b


def restar(a, b):
    print(BIENVENIDA)
    mensaje = "Restando..."  # variable de ámbito local
    print(mensaje)
    return a - b


def multiplicar(a, b):
    print(BIENVENIDA)
    mensaje = "Multiplicando..."  # variable de ámbito local
    print(mensaje)
    return a * b


def dividir(dividendo, divisor):
    print(BIENVENIDA)
    mensaje = "Dividiendo..."  # variable de ámbito local
    print(mensaje)
    if divisor == 0:
        return "No se puede dividir por cero"
    else:
        return dividendo / divisor


funciones = [sumar, restar, multiplicar, dividir]  # variable de ámbito global

numero_1 = float(input("Ingrese el primer número: "))  # variable de ámbito global
numero_2 = float(input("Ingrese el segundo número: "))  # variable de ámbito global

for funcion in funciones:
    resultado = funcion(numero_1, numero_2)  # variable de ámbito global
    print(resultado)

# print(mensaje)  # NameError: name 'mensaje' is not defined
