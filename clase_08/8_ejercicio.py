"""
=========
EJERCICIO
=========
Solicitar al usuario datos sobre un producto:
    - nombre
    - precio
    - cantidad
Guardar en un diccionario y mostrar en la consola:
"El producto < > cuesta $< > y su stock es < >."
* no usar funciones
"""

def ingresar_datos_producto():
    nombre_producto = input("Ingrese el nombre del producto: ")
    precio_producto = float(input("Ingrese el precio del producto: "))
    stock_producto = int(input("Ingrese la cantidad en stock del producto: "))

    datos_producto["nombre_producto"] = nombre_producto
    datos_producto["precio_producto"] = precio_producto
    datos_producto["stock_producto"] = stock_producto
    return datos_producto

def mostrar_datos_producto(producto):
    print(f"El producto {producto["nombre_producto"]} cuesta ${producto["precio_producto"]} y su stock es {producto["stock_producto"]}")


datos_producto = {}
def main():
    datos_producto = ingresar_datos_producto()
    mostrar_datos_producto(datos_producto)

main()