"""
Crear el juego piedra - papel o tijera contra la computadora
"""

import random

opciones = ["piedra", "papel", "tijera"]
partida = 3
juegos_ganados = 0

while True:
    while True:
        jugador = input("Elige piedra, papel o tijera: ").lower().strip()
        if jugador in opciones:
            break

    computadora = random.choice(opciones)
    print("Jugador:", jugador)
    print("Computadora:", computadora)

    if jugador == computadora:
        print("👌 Empate!")
    elif any(
        [
            (jugador == "piedra" and computadora == "tijera"),
            (jugador == "tijera" and computadora == "papel"),
            (jugador == "papel" and computadora == "piedra"),
        ]
    ):
        print("👑 Ganaste!")
        juegos_ganados = juegos_ganados + 1
    else:
        print("😒 Perdiste!")

    partida = partida - 1
    if juegos_ganados == 3:
        print("🍾 Felicidades. Ganaste las 3 partidas")
        break
    elif partida == 0:
        print("😥 Perdiste las 3 partidas. Mejor suerte la próxima vez!")
        break
    else:
        entrada = input("¿Deseas continuar? (n: salir): ")
        if entrada.lower() == "n":
            break
        else:
            continue
