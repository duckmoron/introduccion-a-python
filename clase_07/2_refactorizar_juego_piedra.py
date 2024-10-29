"""
Refactorizar el juego piedra-papel-tijera con funciones
"""

import random


def obtener_jugada_computadora():
    computadora = random.choice(opciones)
    return computadora


def obtener_jugada_jugador():
    while True:
        jugador = input("Elige piedra, papel o tijera: ").lower().strip()
        if jugador in opciones:
            return jugador


def determinar_ganador(jugador, computadora):
    # Devolver "empate", "jugador" o "computadora" según corresponda
    if jugador == computadora:
        return "empate"
    elif (
        (jugador == "piedra" and computadora == "tijera")
        or (jugador == "tijera" and computadora == "papel")
        or (jugador == "papel" and computadora == "piedra")
    ):
        return "jugador"
    else:
        return "computadora"


def mostrar_ganador(jugador, computadora, resultado_juego):
    print("Jugador:", jugador)
    print("Computadora:", computadora)
    if resultado_juego == "empate":
        print("👌 Empate!")
    elif resultado_juego == "jugador":
        print("👑 Ganaste!")
    elif resultado_juego == "computadora":
        print("😒 Perdiste!")
    else:
        print("Resultado inválido")


def main():
    jugador = obtener_jugada_jugador()
    computadora = obtener_jugada_computadora()
    resultado_juego = determinar_ganador(jugador, computadora)
    mostrar_ganador(jugador, computadora, resultado_juego)


opciones = ["piedra", "papel", "tijera"]

main()
