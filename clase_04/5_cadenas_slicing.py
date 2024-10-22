cadena_python = 'Hola Mundo!'
print(cadena_python[0]) #Imprime: 'H', 
print(cadena_python[1]) #Imprime: 'o'

# También se puede usar el índice negativo

print(cadena_python[-1]) # Imprime: '!',
print(cadena_python[-2]) # Imprime: 'd'

# El índice también puede ser un rango

print(cadena_python[0:5]) # Imprime: 'Hola '

# También se puede omitir el inicio o el final del rango

print(cadena_python[:5]) # Imprime: 'Hola '
print(cadena_python[5:]) # Imprime: 'Mundo!'

# También se puede usar un paso

print(cadena_python[::2]) # Imprime: 'HloM!'
print(cadena_python[::-1]) # Imprime: '!dlroW olleH'

# También se puede usar un rango con un paso

print(cadena_python[0:5:2]) # Imprime: 'Hlo'