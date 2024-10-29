"""
Refactorizar el juego del ahorcado: clase 5, ejercicio 1.
"""


def presentacion():
    print("=========================")
    print("✨ JUEGO DEL AHORCADO ✨")
    print("=========================")
    print("¡Bienvenido al juego del ahorcado!")
    print("Tienes que adivinar 3 personajes del Señor de los Anillos.")
    print("Tienes 5 vidas antes de perder")
    print("Los personajes son:", personajes_senor_de_los_anillos)
    print()


def elegir_personaje():
    eleccion_personaje = input("Ingresa el nombre de un personaje: ")
    eleccion_personaje = eleccion_personaje.strip().capitalize()
    if eleccion_personaje in personajes_senor_de_los_anillos:
        return eleccion_personaje
    else:
        return None


def jugar():
    vidas = 5
    personajes_adivinados = 0
    while True:
        print(f"Te restan adivinar {3 - personajes_adivinados} personajes del Señor de los Anillos.")
        print(f"Tienes {vidas} vidas.")
        if vidas == 0:
            print("😒 Has perdido todas tus vidas. ¡Fin del juego!")
            break
        elif personajes_adivinados == 3:
            print("🍾 ¡Felicidades! Has adivinado a 3 personajes. ¡Ganaste!")
            break
        else:
            eleccion_personaje = elegir_personaje()
            if eleccion_personaje:
                personajes_adivinados += 1
                personajes_senor_de_los_anillos.remove(eleccion_personaje)
                print("✨ ¡Correcto! Has adivinado un personaje.")
                continue
            else:
                vidas -= 1
                print("😟 Incorrecto. Ese personaje no está en la lista.")
                continue


def main():
    presentacion()
    jugar()


personajes_senor_de_los_anillos = [
    "Frodo",
    "Sam",
    "Aragorn",
    "Legolas",
    "Gimli",
    "Gandalf",
    "Boromir",
    "Merry",
    "Pippin",
    "Saruman",
    "Sauron",
    "Gollum",
    "Galadriel",
    "Elrond",
    "Bilbo",
]


main()
