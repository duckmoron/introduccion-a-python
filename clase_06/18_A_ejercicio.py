# Transformar el juego ahoracado... en funciones

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

print("=====================")
print("✨      JUEGO     ✨")
print("=====================")

vidas = 5
personajes_adivinados = 0

def eleccion_jugador():
    personaje_usuario = input("Ingresa el nombre de un personaje del Señor de los Anillos: ")
    personaje_usuario = personaje_usuario.strip().capitalize()
    return personaje_usuario

def comparar_respuesta(personaje_usuario):

    if personaje_usuario in personajes_senor_de_los_anillos:
        personajes_senor_de_los_anillos.remove(personaje_usuario)
        return True
    else:
        return False
    
def fin_partida(comparacion):

    global personajes_adivinados
    global vidas

    if comparacion:
        personajes_adivinados += 1
        print("✨ ¡Correcto! Has adivinado un personaje.")
    else:
        vidas -= 1
        print("😟 Incorrecto. Ese personaje no está en la lista.")
    
    if vidas == 0:
        print("😒 Has perdido todas tus vidas. ¡Fin del juego!")
        return
    elif personajes_adivinados == 3:
        print("🍾 ¡Felicidades! Has adivinado a 3 personajes. ¡Ganaste!")
        return
    else:
        print(f"Te restan adivinar {3 - personajes_adivinados} personajes.")
        print(f"Tienes {vidas} vidas.")
        main()

def main():
    
    jugador = eleccion_jugador()
    comparar = comparar_respuesta(jugador)
    fin_partida(comparar)


main()