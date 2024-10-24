BIENVENIDA = "OPERACION"

def sumar(a,b):
    print(BIENVENIDA)
    mensaje = "Sumando..."
    print(mensaje)
    return a + b

def restar(a,b):
    print(BIENVENIDA)
    mensaje = "Restando..."
    print(mensaje)
    return a - b

def multiplicar(a,b):
    print(BIENVENIDA)
    mensaje = "Multiplicando..."
    print(mensaje)
    return a * b
    
def dividir(dividendo,divisor):
    print(BIENVENIDA)
    mensaje = "Dividiendo..."
    print(mensaje)
    if dividendo==0 or divisor==0:
        return "No se puede dividir por cero"
    else:
        return dividendo / divisor
    
        
funciones = [ 
    sumar,
    restar,
    multiplicar,
    dividir
    ]

numero_1 = float(input('Ingrese el primer numero: '))
numero_2 = float(input('Ingrese el segundo numero: '))

for funcion in funciones:
    print(funcion.__name__)
    resultado = funcion(numero_1, numero_2)
    print(resultado)