suma = 0

while True:
    entrada = input("Ingrese x para salir, o un número para sumar: ")
    if entrada == "x":
        break #sale del bucle hacia abajo
        print("Nunca se ejecutará")
    suma = suma + int(entrada)

print(suma)
print("Fin del programa")