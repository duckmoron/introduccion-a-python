class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludar(self): # metodo de instancia
        print(f"Hola, mi nombre es {self.nombre} {self.apellido}!")

def main():
    juan = Persona("Juan", "Pérez")
    maria = Persona(nombre="María", apellido="Gómez")
    juan.saludar()
    maria.saludar()


main()