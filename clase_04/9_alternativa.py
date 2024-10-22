# Alternativa solución

frutas = [
    "manzana",
    "banana",
    "manzana",
    "pera",
    "naranja",
    "sandía",
    "uva",
    "kiwi",
    "mango",
]

while True:
    letra_usuario = input("Ingrese una letra: ")
    if len(letra_usuario) == 1 and letra_usuario.isalpha():
        break

contador = 0
for fruta in frutas:
    contador = contador + fruta.count(letra_usuario)
    # for caracter in fruta:
    #     if caracter == letra_usuario:
    #         contador = contador + 1

if contador > 1:
    print(f"Encontré la letra {letra_usuario} {contador} veces")
elif contador == 1:
    print(f"Encontré la letra {letra_usuario} una vez")
else:
    print(f"No encontré la letra {letra_usuario} en la lista.")

# os.system("pause")
