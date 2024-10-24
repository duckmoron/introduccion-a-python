
# Operaciones

def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def multiplicar(a,b):

    return a * b
    
def dividir(dividendo,divisor):
    if divisor==0:
        return
    else:
        return dividendo / divisor
    

def principal():
    numero_1 = float(input('Ingrese el primer numero: '))
    numero_2 = float(input('Ingrese el segundo numero: '))
        
    funciones = [ 
        sumar,
        restar,
        multiplicar,
        dividir
        ]

    for funcion in funciones:
        print(funcion.__name__)
        resultado = funcion(numero_1, numero_2)
        if resultado is not None:
            print(resultado)
        else:
            print("Hubo un error")
        
principal()