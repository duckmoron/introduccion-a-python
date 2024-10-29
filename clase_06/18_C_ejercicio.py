# Crear un programa que muestre un menú:
# 1. Sumar
# 2. Restar
# 3. Multiplicar
# 4. Dividir
# x. Salir
# Cada operación aritmética tendrá su propia función
# a) Pedir al usuario 2 números
# b) Seleccionar una opción del menú
# c) Mostrar el resultado

# Operaciones

def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def multiplicar(a,b):
    return a * b
    
def dividir(dividendo,divisor):
    if divisor==0:
        return
    else:
        return dividendo / divisor
    
def introducir_numeros():
    n1 = int(input("Ingrese el primer número: "))
    n2 = int(input("Ingrese el segundo número: "))
    return n1, n2 

def introducir_operador():

    print()
    print("MENÚ")
    print("---------------")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("x. Salir")
    print("---------------")
    opciones = ["1", "2", "3", "4", "x"]

    while True:
        operador = input("Seleccionar una opción del menú e ingresá 1,2,3,4 o x: ")
        if operador in opciones:
            return operador

def realizar_operaciones(numero_1, numero_2, operador):
    funciones = [ 
        sumar,
        restar,
        multiplicar,
        dividir
        ]
    
    funcion = funciones[int(operador) -1]
    resultado = funcion(numero_1,numero_2)

    return resultado
    
def mostrar_resultado(resultado):

    print("-")
    print(f"Resultado: {resultado}")
    print("-")

def main():
    numero_1, numero_2 = introducir_numeros()
    operador = introducir_operador()
    if operador != "x":
        resultado = realizar_operaciones(numero_1,numero_2,operador)
        mostrar_resultado(resultado)
    
        
main()