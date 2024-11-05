class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludar(self): # metodo de instancia
        print(f"Hola, mi nombre es {self.nombre} {self.apellido}!")

    def caminar(self, pasos):
        print(f"Yo, {self.nombre}, he dado {pasos} pasos...")

def main():
    juan = Persona("Juan", "Pérez")
    maria = Persona(nombre="María", apellido="Gómez")
    juan.saludar()
    maria.saludar()

    juan.caminar(100)
    maria.caminar(5213)


main()