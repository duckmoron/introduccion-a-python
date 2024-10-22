gran_lista = [10, 50.45, "cadena", True, ["casa", "libro", "árbol"]]

entero = gran_lista[0]

print(f"{entero=}") # si agrego el igual al final, me lo referencia en el print "entero=10"

decimal = gran_lista[1]

print(f"{decimal=}")

cadena = gran_lista[2]

print(f"{cadena=}")

booleano = gran_lista[3]

print(f"{booleano=}")

sub_lista = gran_lista[4]

print(f"{sub_lista=}")

# Para acceder a un elemento de una sub lista

elemento_sub_lista = sub_lista[1]

print(f"{elemento_sub_lista=}") # si agrego el igual al final, me lo referencia en el print "elemento_sub_lista='libro'"

# Para modificar un elemento de una sub lista

sub_lista[1] = "libro modificado"

print(f"{sub_lista=}") # si agrego el igual al final, me lo referencia en el print "sub_lista=['casa', 'libro modificado', 'árbol']"

# Para agregar un elemento a una sub lista

sub_lista.append("nuevo elemento")

print(f"{sub_lista=}") # si agrego el igual al final, me lo referencia en el print "sub_lista=['casa', 'libro modificado', 'árbol', 'nuevo elemento']"

# Para eliminar un elemento de una sub lista

del sub_lista[1]

print(f"{sub_lista=}") # si agrego el igual al final, me lo referencia en el print "sub_lista=['casa', 'árbol', 'nuevo elemento']"

# Para volver a agregar un elemento a una sub lista

sub_lista.insert(1, "elemento insertado")

print(f"{sub_lista=}") # si agrego el igual al final, me lo referencia en el print "sub_lista=['casa', 'elemento insertado', 'árbol', 'nuevo elemento']"

# Para recorrer una lista

for elemento in sub_lista:

    print(f"{elemento=}")

# Para recorrer una lista en posiciones inversas

for elemento in reversed(sub_lista):

    print(f"{elemento=}")

# Para recorrer una lista en posiciones pares

for elemento in sub_lista[::2]:

    print(f"{elemento=}")

# Para recorrer una lista en posiciones impares

for elemento in sub_lista[1::2]:

    print(f"{elemento=}")

# Para recorrer una lista en orden ascendente

sub_lista.sort()

print(f"{sub_lista=}")

# Para recorrer una lista en orden descendente

sub_lista.sort(reverse=True)

print(f"{sub_lista=}")

# Para buscar un elemento en una lista

elemento_buscado = "elemento insertado"

if elemento_buscado in sub_lista:

    print(f"{elemento_buscado} está en la lista")

