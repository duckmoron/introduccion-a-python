# Las tuplas son colecciones de datos que son inmutables
mi_tupla = (1, 2, 3, 4, 5, 4, 4)
print(mi_tupla)
print(type(mi_tupla))
print(mi_tupla)
print(len(mi_tupla))
print(mi_tupla[0])
print(mi_tupla[0:3])
cuenta = mi_tupla.count(4)
print(f"{cuenta=}")
indice = mi_tupla.index(4)
print(f"{indice=}")
mi_lista: list = [1, 2, 3, 4, 5, 4, 4]
print(mi_lista)
mi_lista.remove(1)
mi_tupla = tuple(mi_lista)
print(mi_tupla)
tupla_un_elemento = (1000,)
print("Tupla con un solo elemento:", tupla_un_elemento)