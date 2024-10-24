variable_global = "Esta variable puede ser vista desde cualquier función"

def funcion():
    variable_local = "Esta variable solo puede ser vista dentro de esta función"
    mensaje = f"Variable local: {variable_local}"
    print("-" * len(mensaje))
    print(mensaje)
    print("-" * len(mensaje))
    
funcion()