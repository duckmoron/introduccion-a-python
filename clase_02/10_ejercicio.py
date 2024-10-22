"""
A partir del siguiente código,

- Poner un precio a cada producto.
- Crear una billetera con saldo con input()
- Debitar de la billetera el precio del producto seleccionado.
- Mostrar el saldo restante de la billetera.

presentación = (
    "¡Bienvenido al café!\n"
    "Estos son los postres que disponemos:\n"
    "1. Tarta de manzana\n"
    "2. Flan de coco\n"
    "3. Helado de vainilla\n"
)

print(presentación)
pedido = input("¿Qué postre desea pedir? ")

if pedido == "1":
    mensaje = "Pedido recibido. ¡Disfrute de su tarta de manzana!"
elif pedido == "2":
    mensaje = "Pedido recibido. ¡Disfrute de su flan de coco!"
elif pedido == "3":
    mensaje = "Pedido recibido. ¡Disfrute de su helado de vainilla!"
else:
    mensaje = f"Lo siento, {pedido} no está en el menú."

print(mensaje)
"""

precio_tarta = 5
precio_flan = 3
precio_helado = 2

saldo = float(input("¿Cuál es tu saldo?: "))

presentación = (
    "¡Bienvenido al café!\n"
    "Estos son los postres que disponemos:\n"
    f"1. Tarta de manzana: ${precio_tarta}\n"
    f"2. Flan de coco: ${precio_flan}\n"
    f"3. Helado de vainilla: ${precio_helado}\n"
)
print(presentación)
pedido = input("¿Qué postre desea pedir? ")

compra = False  # esto indica que la compra no se ha efectuado
if pedido == "1" and saldo >= precio_tarta:
    saldo = saldo - precio_tarta
    mensaje = "Pedido recibido. ¡Disfrute de su tarta de manzana!"
    compra = True  # se ha efectuado la compra
elif pedido == "2" and saldo >= precio_flan:
    saldo = saldo - precio_flan
    mensaje = "Pedido recibido. ¡Disfrute de su flan de coco!"
    compra = True  # se ha efectuado la compra
elif pedido == "3" and saldo >= precio_helado:
    saldo = saldo - precio_helado
    mensaje = "Pedido recibido. ¡Disfrute de su helado de vainilla!"
    compra = True  # se ha efectuado la compra

if compra == True:  # si se ha efectuado la compra, mostramos el saldo restante
    print(mensaje)
    print(f"Su saldo restante es: ${saldo}")
else:  # si no se ha efectuado la compra, mostramos un mensaje de error
    print(f"Lo siento, {pedido} no está en el menú o no tiene saldo suficiente.")
