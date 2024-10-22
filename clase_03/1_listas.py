# Listas

lista = [12, 3.14, "cadena", True, [1,2,3]]
longitud_lista = len(lista)
print(lista, longitud_lista)

lista_de_frutas = ["ananá", "frutilla", "manzana", "naranja"]
existe_manzana = "manzana" in lista_de_frutas

if existe_manzana:
    print("La fruta 'manzana' existe en la lista.")
else:
    print("La fruta 'manzana' no existe en la lista.")
    
lista_vacia = []
print(lista_vacia, len(lista_vacia))

