# Ejercicio con funciones con parámetros predeterminados
# Crear una función dividir que reciba dos parámetros, uno opcional y otro obligatorio,
# y devuelva el resultado de la división de ambos. Si se pasa un solo argumento,
# dividir / 1.

def dividir(a,b=1):
    if b==0:
        print("No se puede dividir por cero")
    else:
        print(float(a / b))
    
dividir(6)
dividir(6,2)
dividir(8,0)