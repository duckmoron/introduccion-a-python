"""
range()
Es una función que genera un conjunto de números en un rango especificado.
Puedes usarlo para iterar sobre una secuencia de números en un bucle for.
Parámetros:
- start (opcional): El número en el que comenzará la secuencia. Por defecto es 0.
- stop: El número en el que terminará la secuencia (es excluyente).
- step (opcional): El incremento entre cada número en la secuencia. Por defecto es 1.
"""
secuencia = range(10)
print(secuencia)
print(tuple(secuencia))
print(list(secuencia))
print("🔥 start=0, stop=10, step=1")
for i in range(10):
    print(i)
print("🔥 start=1, stop=10, step=1")
for i in range(1, 10):
    print(i)
print("🔥 start=1, stop=10, step=2")
for i in range(1, 10, 2):
    print(i)