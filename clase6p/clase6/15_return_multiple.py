def sumar(n1, n2):
    return n1 + n2


def introducir_numeros():
    n1 = int(input("Introduce el primer número: "))
    n2 = int(input("Introduce el segundo número: "))
    return n1, n2


numero1, numero2 = introducir_numeros()  # Desempaquetamos la tupla en dos variables


resultado = sumar(numero1, numero2)
print(f"La suma de {numero1} y {numero2} es {resultado}")
