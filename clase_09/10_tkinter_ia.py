from tkinter import Entry, Label, Tk, messagebox

def mostrar_bienvenida(event):
    nombre = caja.get()
    if nombre:
        messagebox.showinfo("Bienvenida", f"¡Bienvenido, {nombre}!")
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingresa tu nombre.")

def configurar_interfaz_usuario():
    mi_aplicacion.title("Mi primera app con Tkinter")
    mi_aplicacion.geometry("400x300")
    etiqueta = Label(text="Ingresa tu nombre: ", font=("Arial", 18))
    etiqueta.place(x=20, y=20)
    global caja
    caja = Entry(font=("Arial", 18))
    caja.place(x=20, y=60, width=200, height=25)
    caja.bind("<Return>", mostrar_bienvenida)  # Asigna el evento Enter a la función

mi_aplicacion = Tk()
configurar_interfaz_usuario()
mi_aplicacion.mainloop()