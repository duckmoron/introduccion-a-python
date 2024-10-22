# Entrada
standard_input = 'hello world'; 
edad = int(input("Por favor, ingresa tu edad: "))

# Operación

if edad < 0:
    mensaje = "La edad no puede ser negativa"
else:
    if edad >= 18:
        mensaje = "eres mayor de edad"
    else:
        mensaje = "eres menor de edad"

# Salida
print(mensaje)