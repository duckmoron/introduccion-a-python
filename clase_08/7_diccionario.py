# Un diccionario es una colección de pares clave-valor.
# Los pares clave-valor se separan con dos puntos (:) y los pares se separan con comas (,).
# Son mutables, lo que significa que se pueden cambiar sus valores una vez creados.

diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print(diccionario)
print(type(diccionario))
print(len(diccionario))
# cómo saber si existe una clave en el diccionario
print("nombre" in diccionario)
print("telefono" in diccionario)
# acceder a valores de un diccionario
# print(diccionario["nombre"])
nombre = diccionario["nombre"]
edad = diccionario["edad"]
ciudad = diccionario["ciudad"]
print(f"{nombre} tiene {edad} años y vive en {ciudad}")
print(f"{diccionario["nombre"]} tiene {diccionario["edad"]} años y vive en {diccionario["ciudad"]}")
# cambiando valores de un diccionario
diccionario["edad"] += 1
print(diccionario)
# crear un elemento más (un par clave:valor)
diccionario["telefono"] = "123456789"
print(diccionario)
# eliminar un elemento del diccionario
del diccionario["telefono"]
print(diccionario)