"""
A partir de la siguiente función, crear un encabezado y pie con
signos, como por ejemplo:
*******************************
Bienvenido a la ciudad de Luján
*******************************
Se tiene que adapatar a la longitud de la cadena
def dar_bienvenida(ciudad):
    print(f"Bienvenido a la ciudad de {ciudad}")

nombre_ciudad = input("Nombre de tu ciudad: ")
dar_bienvenida(nombre_ciudad)
"""

def dar_bienvenida(ciudad):
    mensaje = f"Bienvenido a la ciudad de {ciudad}"
    adorno = "-" * len(mensaje)
    # print(adorno)
    # print(mensaje)
    # print(adorno)
    print(f"{adorno}\n{mensaje}\n{adorno}")

nombre_ciudad = input("Nombre de tu ciudad: ")
dar_bienvenida(nombre_ciudad)