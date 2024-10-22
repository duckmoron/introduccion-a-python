"""
A partir de la siguiente lista, 
imprimir cuántas veces está una determinada letra 
la cual es ingresada desde input(). 
Si la encuentra varias veces, imprimir
    'Encontré la letra x tantas veces"'
Si la encontró una vez:
    'Encontré la letra x una vez'
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
"""

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
    letra_buscada = input("Ingrese una letra: ")
    if len(letra_buscada) == 1 and letra_buscada.isalpha():
        break

veces_encontrada = 0

for fruta in frutas:
    for caracter in fruta:
        if caracter == letra_buscada:
            veces_encontrada += 1

if veces_encontrada > 1:
    print(f"Encontré la letra '{letra_buscada}' tantas veces: {veces_encontrada}")
else:
    print(f"Encontré la letra '{letra_buscada}' una vez")

# os.system("pause")