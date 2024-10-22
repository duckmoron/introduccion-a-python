"""
Crear un contador que vaya disminuyendo su valor
de uno en uno desde 10 a 0
mientras se imprime por pantalla
"""
from time import sleep

i = 10
while i > 0:
    sleep(0.5)
    print(i)
    i = i - 1
else:
    print("¡El contador ha terminado!")
