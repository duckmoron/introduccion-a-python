entrada = input('Introduce un número entero: ')
if entrada.isdecimal():
    numero = int(entrada)
    print(f'Has ingresado un número entero: {numero}')
else:
    print('No has ingresado un número entero.')