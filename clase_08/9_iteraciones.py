productos = {
    "pan": 10,
    "leche": 20,
    "huevos": 30,
}


print("✨ claves")
for k in productos.keys():
    print(k)

print("✨ valores")
for v in productos.values():
    print(v)

print("✨ clave, valor")
for k, v in productos.items():
    print(f"Producto: {k} ${v:.2f}")
