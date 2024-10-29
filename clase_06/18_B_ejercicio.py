# Transformar el juego piedra... en funciones

import random


def eleccion_computadora():
    computadora = random.choice(opciones)
    print(f"La computadora eligió: {computadora}")
    return computadora

def eleccion_jugador():

    while True:
        jugador = input("Elige piedra, papel o tijera: ").lower().strip()
        if jugador in opciones:
            # print(f"jugador: {jugador}")
            return jugador

def juego(jugador, computadora):

    if jugador == computadora:
        print("👌 Empate!")
        fin_partida("empate")
        return
    elif any(
        [
            (jugador == "piedra" and computadora == "tijera"),
            (jugador == "tijera" and computadora == "papel"),
            (jugador == "papel" and computadora == "piedra"),
        ]
    ):
        print("👑 Ganaste!")
        fin_partida("gano")
        return
    else:
        print("😒 Perdiste!")
        fin_partida("perdio")
        return

def fin_partida(resultado):
    global partida
    global juegos_ganados

    if resultado == "gano":
        juegos_ganados += 1
        print(f"Has ganado {juegos_ganados} partidas")
    elif resultado == "perdio":
        partida -= 1
        print(f"Perdiste, te quedan {partida} vidas.")

    if juegos_ganados == 3:
        print("🍾 Felicidades. Ganaste 3 partidas")
        return
    elif partida == 0:
        print("😥 Perdiste 3 partidas. Mejor suerte la próxima vez!")
        return
    else:
        entrada = input("¿Deseas continuar? (n: salir): ")
        if entrada.lower() == "n":
            return
        else:
            main()

def main():
    jugador = eleccion_jugador()
    computadora = eleccion_computadora()
    juego(jugador,computadora)



opciones = ["piedra", "papel", "tijera"]

partida = 3
juegos_ganados = 0

main()