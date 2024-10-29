"""
Escribir un programa que almacene las notas de por lo menos 5 asignaturas
de un estudiante en una tupla.
Calcular la media de las notas y mostrar las notas y el promedio
Usar las funciones (hasta 4)
"""

def notas_estudiante(materias):
    notas = []
    for materia in materias:
        while True:
            nota = int(input(f"Introduce la nota de {materia.upper()}: "))
            if nota < 0 or nota > 10:
                mensaje = "La nota debe estar entre 0 y 10."
                print(mensaje)
                continue
            else:
                notas.append(nota)
                break
    return tuple(notas)

def calcular_promedio(notas):
    suma_notas = sum(notas)
    return suma_notas / len(notas)

def main():
    materias = ["matematicas","lengua","ingles","plastica","musica"]
    notas = notas_estudiante(materias)
    promedio = calcular_promedio(notas)
    titulo = "Notas del estudiante:"
    lineas = "-" * len(titulo)

    print(lineas)
    print(titulo)
    print(lineas)

    posicion_materia = 0
    for materia in materias:
        print(f"{materia.upper()}: {notas[posicion_materia]}")
        posicion_materia += 1
        
    print(lineas)
    print(f"Promedio: {promedio}")

main()