
from time import sleep
def bienvenida_ciudad(ciudad):
    for letra in ciudad:
        print(letra, end=" ", flush=True)
        sleep(0.2)
    print()

mis_ciudades = ["Buenos Aires", "Córdoba", "Rosario"]
for ciudad in mis_ciudades:
    bienvenida_ciudad(ciudad)

# mi_ciudad = input("¿Cuál es tu ciudad? ")
# bienvenida_ciudad(mi_ciudad)