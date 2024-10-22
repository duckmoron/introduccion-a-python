"""
Crear el juego piedra, papel y tijera contra la computadora.
"""

import random

opciones = ["piedra", "papel", "tijera"]


while True:
    jugador = input("Elige piedra, papel o tijera: ").lower().strip()
    if jugador in opciones:
        break
    print("elige una opción correcta")

computadora = random.choice(opciones)
print("Jugador:", jugador)
print("Computadora:", computadora)

# piedra > tijera
# papel > piedra
# tijera > papel

if (jugador == "piedra" and computadora == "tijera") or \
   (jugador == "papel" and computadora == "piedra") or \
   (jugador == "tijera" and computadora == "papel"):
    print("Ganaste!")
elif jugador == computadora:
    print("Empataste!")
else:
    print("Perdiste!")