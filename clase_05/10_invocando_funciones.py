def hola():
    print("hola")

def adios():
    print("adios")

saludos = [hola, adios, hola, hola] # la funcion no se invoca por no tener (), hola(), adios()... la ejecuto despues en el "for ir"

for saludo in saludos:
    print("🔥 Invocando función:")
    saludo()