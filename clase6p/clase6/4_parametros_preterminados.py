def saludar(nombre, apellido=""):
    # print(f"Tu nombre es {nombre}")
    # print(f"Tu apellido es {apellido}")
    if apellido:
        print(f"Tu nombre completo es {nombre} {apellido}")
    else:
        print(f"Tu nombre es {nombre}")


saludar("Juan")
saludar("Juan", "Pérez")
