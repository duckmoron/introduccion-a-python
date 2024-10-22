suma = 0

while True:
    entrada = input("Ingrese x para salir, o un número para sumar: ")
    if entrada == "x":
        break  # sale del bucle hacia abajo
    if entrada.isdigit():
        suma = suma + int(entrada)
    else:
        print("Entrada inválida. Intente de nuevo.")
        continue  # vuelve al inicio del bucle
        print("Nunca se va ejecutar")

print(suma)
print("Fin del programa")
