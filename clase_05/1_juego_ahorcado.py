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

vidas = 5
personajes_adivinados = 0

print("=====================")
print("✨      JUEGO     ✨")
print("=====================")


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
        personaje_usuario = input("Ingresa el nombre de un personaje: ")
        personaje_usuario = personaje_usuario.strip().capitalize()
        if personaje_usuario in personajes_senor_de_los_anillos:
            personajes_adivinados += 1  # personajes_adivinados = personajes_adivinados + 1
            personajes_senor_de_los_anillos.remove(personaje_usuario)
            print("✨ ¡Correcto! Has adivinado un personaje.")
            continue
        else:
            vidas -= 1  # vidas = vidas - 1
            print("😟 Incorrecto. Ese personaje no está en la lista.")
            continue
