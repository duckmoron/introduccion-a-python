"""
Preguntar al usuario su ciudad
Definir una función que dé la bienvenida a una ciudad
Mostrar el mensaje de bienvenida
"""


def bienvenida_ciudad(ciudad):
    print(f"Bienvenido a {ciudad}.")

mi_ciudad = input("¿Cuál es tu ciudad? ")
bienvenida_ciudad(mi_ciudad)