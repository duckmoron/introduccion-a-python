variable_global = "Esta variable puede ser vista desde cualquier función"


def funcion():
    variable_local = "Esta variable solo puede ser vista dentro de la función"
    print(variable_local)
    print("-" * len(variable_local))
    print(variable_global)
    print("-" * len(variable_global))


funcion()

# print(variable_local)  # Esto daría un error porque variable_local solo existe dentro de la función
