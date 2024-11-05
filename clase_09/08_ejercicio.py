"""
✨✨✨ EJERCICIO  ✨✨✨ 
Crear una clase Producto.
Sus atributos: nombre: str, precio: float
Su método: incrementar_precio(porcentaje: float)
Este método va a incrementar el precio, recibiendo un porcentaje para hacerlo
Usar main() para instanciar la clase y probar el método.
"""
class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio
        
    def incrementar_precio(self, porcentaje: float):
        """ Incrementa el precio del producto en el porcentaje indicado."""
        self.precio += self.precio * (porcentaje / 100)
        return self.precio
    
def main():
    producto = Producto("Camisa", 20.0)
    print(f"Precio inicial: {producto.precio}")
    producto.incrementar_precio(15)
    print(f"Precio final: {producto.precio}")

main()