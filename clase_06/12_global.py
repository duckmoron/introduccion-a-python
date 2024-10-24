variable_global ="¡!"

def cambiar_global():
    variable_global = "a" # Esto crea una nueva variable local! NO cambia a la global
    print(variable_global)
    
cambiar_global()
print(variable_global)