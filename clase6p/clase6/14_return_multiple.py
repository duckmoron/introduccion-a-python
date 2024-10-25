def sumar(n1, n2):  # n1 y n2 son parámetros
    return n1 + n2


def introducir_numeros():
    n1 = int(input("Introduce el primer número: "))
    n2 = int(input("Introduce el segundo número: "))
    return n1, n2  # devuelve una tupla


tupla = introducir_numeros()
print(tupla)
print(type(tupla))

n1 = tupla[0]
n2 = tupla[1]

resultado = sumar(n1, n2)  # n1 y n2 son argumentos
print(f"La suma de {n1} y {n2} es {resultado}")
