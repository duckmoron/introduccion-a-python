# Entrada
edad = int(input("Por favor, ingresa tu edad: "))

# Operación

if edad < 0:
    mensaje = "La edad no puede ser negativa"
elif edad < 13:
    mensaje = "eres niño"
elif edad < 18:
    mensaje = "eres adolescente"
elif edad < 65:
    mensaje = "eres adulto"
elif edad < 120:
    mensaje = "eres adulto mayor"
else:
    mensaje = "quizás haya un problema con la edad"

# Salida
print(mensaje)