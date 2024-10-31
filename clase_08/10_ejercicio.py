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