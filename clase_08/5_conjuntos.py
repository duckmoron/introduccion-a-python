# Los conjuntos son una colección de elementos desordenada de datos únicos (no tendrá duplicados)
# Son mutables, es decir, que se pueden modificar.
# No admite (objetos no hasheables: inmutables, por ej. listas, conjuntos, diccionarios)
entero = 0
lista = []
tupla = ()
# conjunto = {1, 2, 3, True, "Hola", 3.14, entero, tupla, "hola", "Hola", lista}
conjunto = {1, 2, 3, True, "Hola", 3.14, entero, tupla, "hola", "Hola"}
print(conjunto)
print(type(conjunto))
conjunto_vacio = set()
print(f"{conjunto_vacio=} - {type(conjunto_vacio)=} - {len(conjunto_vacio)=}")
conjunto_a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
conjunto_a.add(10)
print(conjunto_a)
conjunto_a.remove(10)  # Si no existe el elemento a eliminar, da error
if 10 in conjunto_a:
    conjunto_a.remove(10)
print(conjunto_a)
conjunto_a.discard(9)
conjunto_a.discard(9)  # No da error si no existe el elemento a eliminar
print(conjunto_a)