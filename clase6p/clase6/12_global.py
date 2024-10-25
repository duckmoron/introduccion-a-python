variable_global = "¡!"


def cambiar_global():
    # variable_global = "a"  # crea una variable local, no cambia a la global
    # print(variable_global)  # ¿Qué se imprime? -> la variable local: "a"
    global variable_global
    variable_global = "a"


cambiar_global()
print(variable_global)
