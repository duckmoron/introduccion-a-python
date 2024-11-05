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


def comprar(carrito_compras):
    while True:
        productos_a_comprar_input = input("¿Cuantos productos desea comprar? ")
        if productos_a_comprar_input.isdecimal():
            productos_a_comprar = int(productos_a_comprar_input)
            break
        else:
            print("Error, debe ingresar un número entero")
            continue

    for i in range(productos_a_comprar):
        producto = input("Nombre: ")
        precio = float(input("Precio: "))
        cantidad = float(input("Cantidad: "))
        datos = {
            "producto": producto,
            "precio": precio,
            "cantidad": cantidad,
        }
        carrito_compras.append(datos)

def ver_lista_compras(carrito_compras):
    print("\n🍾 Carrito de compras:")
    if len(carrito_compras) == 0:
        print("No hay productos en el carrito")
        return
    else:
        for producto in carrito_compras:
            # print(f"Producto: {producto['producto']}, Precio: ${producto['precio']}, Cantidad: {producto['cantidad']}")
            
            print()
            for clave, valor in producto.items():
                if clave == "precio":
                    print(f"{clave.upper()}: ${valor:.2f}")
                else:
                    print(f"{clave.upper()}: {valor}")

def main():

    carrito_compras = []

    comprar(carrito_compras)
    ver_lista_compras(carrito_compras)

main()
