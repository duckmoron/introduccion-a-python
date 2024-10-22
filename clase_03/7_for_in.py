letras = ["a", "b", "c"]
iterador = 0

for letra in letras:
    letras[iterador] = letras[iterador].upper()
    iterador = iterador + 1

print(letras)