# Crear una clase llamada Persona que tenga dos atributos: nombre y apellido
# Crear 2 objetos (instancias) de Persona y mostrar sus atributos con print()

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
def listar_personas(personas):
    for persona in personas:
        print(f"Nombre: {persona.nombre}, Apellido: {persona.apellido}")
def main():
    persona1 = Persona("Juan", "Pérez")
    persona2 = Persona("Pepe", "Grillo")
    personas = [persona1, persona2]
    listar_personas(personas)

main()