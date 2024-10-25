"""
Crear una función que imprima un apellido en maýusculas,
seguido de una coma, un espacio, y el nombre de la persona
con el primer caracter en mayúsculas y el resto en minúsculas

Crear una lista de nombres de personas, y usar la función para ver la lista
"""


def imprimir_nombre(nombre, apellido):
    cadena = f"{apellido.upper()}, {nombre.capitalize()}"
    print(cadena)


persona_1 = ["juan", "perez"]
persona_2 = ["maria", "gomez"]
persona_3 = ["luis", "rodriguez"]

lista_personas = [persona_1, persona_2, persona_3]

for persona in lista_personas:
    nombre = persona[0]
    apellido = persona[1]
    imprimir_nombre(nombre, apellido)
