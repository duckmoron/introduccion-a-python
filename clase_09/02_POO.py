# las clases no llevan parentesis al definirlas.
class Usuario:
    def __init__(self, email, contraseña): # metodo constructor
        self.email = email
        self.contraseña = contraseña

# Crear un usuario
# Al invocar la clase si lleva parentesis.
usuario_1 = Usuario("juan@mail", "juan123")
usuario_2 = Usuario("lucas@mail", "lucas789")

# Mostrar los datos del usuario
print(usuario_1.email, usuario_1.contraseña)
print(usuario_2.email, usuario_2.contraseña)