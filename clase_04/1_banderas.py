suma = 0

bandera = True # tecnica de bandera o flag

while bandera: #while bandera == true
    entrada = input("Ingrese x para salir, o un número para sumar: ")
    if entrada == "x":
        bandera = False  # sale del bucle hacia abajo
    elif entrada.isdigit():
        suma = suma + int(entrada)
    else:
        print("Entrada inválida. Intente de nuevo.")
        continue  # vuelve al inicio del bucle

print(f"Suma TOTAL: {suma}")
