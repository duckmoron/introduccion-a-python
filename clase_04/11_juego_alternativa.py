"""
Crear el juego piedra, papel y tijera contra la computadora.
"""

import random

opciones = ["piedra", "papel", "tijera"]
partidas = 3
juegos_ganados = 0

while True:
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

    if any(
        [
            (jugador == "piedra" and computadora == "tijera"),
            (jugador == "papel" and computadora == "piedra"),
            (jugador == "tijera" and computadora == "papel")
        ]
    ):
        print("Ganaste!")
        juegos_ganados += 1
    elif jugador == computadora:
        print("Empataste!")
    else:
        print("Perdiste!")

    partidas -= 1
    if juegos_ganados == 3:
        print("Felicitaciones. Ganaste las 3 partidas")
        break
    elif partidas == 0:
        print("Has perdido todas las partidas")
    else:
        entrada = input("Deseas continua? (s/n): ")