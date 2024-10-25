"""
Escribir un programa que almacene las notas de por lo menos 5 asignaturas
de un estudiante en una tupla.
Calcular la media de las notas y mostrar las notas y el promedio
Usar las funciones (hasta 4)
"""

def pedir_notas():
    mensaje = "La nota debe estar entre 0 y 10."
    while True:
        m1 = int(input("Introduce la nota de MATEMATICAS: "))
        if m1 < 0 or m1 > 10:
            print(mensaje)
            continue
        m2 = int(input("Introduce la nota de LENGUA: "))
        if m2 < 0 or m2 > 10:
            print(mensaje)
            continue
        m3 = int(input("Introduce la nota de INGLES: "))
        if m3 < 0 or m3 > 10:
            print(mensaje)
            continue
        m4 = int(input("Introduce la nota de MUSICA: "))
        if m4 < 0 or m4 > 10:
            print(mensaje)
            continue
        m5 = int(input("Introduce la nota de PLASTICA: "))
        if m5 < 0 or m5 > 10:
            print(mensaje)
            continue
        else:
            return m1,m2,m3,m4,m5

notas_estudiante = pedir_notas()
print(notas_estudiante)

# def validar_nota():


# def calcular_promedio(notas):
#     pass


