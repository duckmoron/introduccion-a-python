def sumar(n1, n2):
    return n1 + n2

def introducir_numeros():
    n1 = int(input("Ingrese el primer número: "))
    n2 = int(input("Ingrese el segundo número: "))
    return n1, n2 # devuelve una tupla (n1, n2) ES INMUTABLE!

# resultado = sumar(100, 20)
# print(resultado)

tupla = introducir_numeros()
print(tupla)
print(type(tupla))

n1 = tupla[0]
n2 = tupla[1]

resultado = sumar(n1, n2)
print(f"La suma de {n1} y {n2} es {resultado}")