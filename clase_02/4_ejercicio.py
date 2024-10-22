"""

Ejercicio:

Pedir al usuario su edad.

Si es mayor o igual a 18, imprimir "eres mayor de edad"

De lo contrario, imprimir "eres menor de edad"

"""

# Entrada
edad = int(input("Ingresa tu edad: "))

# Operacion
if edad >= 18: 
    mensaje = "eres mayor de edad"
else : 
    mensaje = "eres menor de edad"
    
# Salida
print(mensaje) 