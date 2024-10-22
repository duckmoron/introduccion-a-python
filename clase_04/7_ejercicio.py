entrada = input("Introduce un número entero: ")
entrada = entrada.strip()  # quita los espacios antes y despues de los caracteres
caso_positivo = entrada.isdecimal()
caso_negativo = entrada[0] == "-" and entrada[1:].isdecimal()
if caso_positivo or caso_negativo:
    numero = int(entrada)
    print(f"Has introducido el número {numero}")
else:
    print("No has introducido un número entero")