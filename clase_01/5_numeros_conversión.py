# Números y conversión de números

print(type(100))  # enteros (int)
print(type(100.23))  # decimales (float)
print(type(100.23j))  # complejo (complex)

entrada_1 = input("Introduce el número 1: ")
entrada_2 = input("Introduce el número 2: ")
intento_de_suma = entrada_1 + entrada_2
print(intento_de_suma)  # los concatena

numero_1 = int(entrada_1)  # conversión de tipos se llama casting
numero_2 = int(entrada_2)
resultado = numero_1 + numero_2  # tecla f2 cambia el nombre de variables
print(f"El resultado de la suma de {numero_1} y {numero_2} es {resultado}")