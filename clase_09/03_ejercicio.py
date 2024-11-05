# Crear una clase llamada Persona que tenga dos atributos: nombre y apellido
# Crear 2 objetos (instancias) de Persona y mostrar sus atributos con print()

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

persona1 = Persona("Juan", "Pérez")
persona2 = Persona("Pepe", "Grillo")

print(f"Nombre: {persona1.nombre}, Apellido: {persona1.apellido}")
print(f"Nombre: {persona2.nombre}, Apellido: {persona2.apellido}")