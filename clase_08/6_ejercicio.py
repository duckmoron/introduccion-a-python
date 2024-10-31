# =============
# ✨ EJERCICIO
# =============
# crear un conjunto con 5 colores: rojo, celeste, azul, blanco, amarillo
# agregar un color al conjunto: verde
# eliminar un color del conjunto con remove: celeste
# eliminar un color del conjunto con remove: violeta
# eliminar un color del conjunto con discard: blanco
# crear un conjuntos con 5 colores más: naranja, marrón, lila, negro, rosa
# unir los dos conjuntos en uno solo: conjunto_final

colores = {"rojo", "celeste", "azul", "blanco", "amarillo"}
print(colores)
colores.add("verde")
print(colores)
colores.remove("celeste")
print(colores)
if "violeta" in colores:
    colores.remove("violeta")
print(colores)
colores.discard("blanco")
print(colores)
mas_colores = {"naranja", "marrón", "lila", "negro", "rosa"}
print(mas_colores)
conjunto_colores = colores.union(mas_colores)

# imprimir el resultado
print(conjunto_colores)  # imprime el conjunto final
