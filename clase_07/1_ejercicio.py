"""
Escribir un programa que almacene las notas de por lo menos 5 asignaturas
de un estudiante en una tupla.
Calcular la media de las notas y mostrar las notas y el promedio
Usar las funciones (hasta 4)
"""


def ingresar_notas():
    nota1 = float(input("Ingrese la nota de la asignatura 1: "))
    nota2 = float(input("Ingrese la nota de la asignatura 2: "))
    nota3 = float(input("Ingrese la nota de la asignatura 3: "))
    nota4 = float(input("Ingrese la nota de la asignatura 4: "))
    nota5 = float(input("Ingrese la nota de la asignatura 5: "))
    return nota1, nota2, nota3, nota4, nota5


def calcular_promedio(notas):
    promedio = sum(notas) / len(notas)
    return promedio


def mostrar_resultados(notas, promedio):
    print("Las notas son las siguientes:", notas)
    print("El promedio de las notas es:", promedio)


def main():
    notas = ingresar_notas()
    promedio = calcular_promedio(notas)
    mostrar_resultados(notas, promedio)


main()
