"""
A partir del siguiente código, utilizar range() para preguntar cuántos invitados
vendrán a la fiesta. 
Luego, utilizar un bucle for para preguntar el nombre de cada uno
y guardarlo en una lista. Ordenarlos alfabéticamente (opcional)
Finalmente, convertir la lista a una tupla y mostrar la lista de invitados iterando sobre ellos
def saludar(nombre):
    print(f"¡Bienvenido {nombre}!")

lista_de_invitados = []
for invitado in lista_de_invitados:
    saludar(invitado)
"""

def obtener_numero_invitados():
    """Pide al usuario el número de invitados y devuelve ese número."""
    numero_invitados = int(input("¿Cuántos invitados vendrán a la fiesta?: "))
    return numero_invitados

def crear_lista_invitados(cantidad):
    """Crea una lista de invitados con el nombre de cada invitado."""
    lista_de_invitados = []
    for i in range(cantidad):
        nombre = input(f"¿Cuál es el nombre del invitado numero {i+1}?: ").strip().capitalize()
        lista_de_invitados.append(nombre)

    lista_de_invitados.sort()
    return lista_de_invitados

def convertir_a_tupla(lista):
    """Convierte una lista a una tupla"""
    tupla_invitados = tuple(lista)
    return tupla_invitados

def saludar_invitados(tupla):
    """Muestra la lista de invitados saludando a cada uno."""
    print()
    print("LISTA DE INVITADOS")
    print("------------------")
    for nombre in tupla:
        print(f"Bienvenido '{nombre}'!")

def main():
    num_invitados = obtener_numero_invitados()
    lista_de_invitados = crear_lista_invitados(num_invitados)
    tupla_invitados = convertir_a_tupla(lista_de_invitados)
    saludar_invitados(tupla_invitados)

main()