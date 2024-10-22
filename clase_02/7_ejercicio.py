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