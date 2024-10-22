"""
A partir de la siguiente matriz, agregar a cada lista, el número 10
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
"""
# Alternativa 1

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

matriz[0].append(10)
matriz[1].append(10)
matriz[2].append(10)

print(matriz)

# Alternativa 2

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

for sublista in matriz:
    sublista.append(10)

print(matriz)

# EXTRA

suma = 0
for i in matriz:
    for u in i:
        suma += u
    i.append(suma)
    suma = 0
    print(i)
