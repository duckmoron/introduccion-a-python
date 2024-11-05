"""
A partir del siguiente código solicitar 3 formularios (usar range())
y guardar cada formulario en una lista llamada carrito_compras
producto = input("Nombre: ")
precio = float(input("Precio: "))
cantidad = float(input("Cantidad: "))
datos = {
    "producto": producto,
    "precio": precio,
    "cantidad": cantidad,
}
print(f"El producto {datos['producto']} cuesta $ {datos['precio']} y su stock es {datos['cantidad']}")
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

    print("Carrito de compras:")
    print()
    for i in range(len(producto)):
        print(f"Producto {i}: {producto[i]['nombre_producto']}, Precio: ${producto[i]['precio_producto']}, Cantidad: {producto[i]['stock_producto']}")
    print()


datos_producto = {}
carrito_compras = []
def main():
    for i in range(3):
        print("---------------------------------")
        print(f"INGRESE LOS DATOS DEL PRODUCTO {i+1}:")
        print("---------------------------------")
        datos_producto = ingresar_datos_producto()
        carrito_compras.append(datos_producto)
    print()
    mostrar_datos_producto(carrito_compras)

main()