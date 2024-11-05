from tkinter import Entry, Tk, Label

def configurar_interfaz_usuario():
    mi_aplicacion.title("Mi primera app con Tkinter")
    mi_aplicacion.geometry("400x300")
    mi_etiqueta = Label(text="Ingresa tu nombre: ", font=("Arial", 18))
    mi_etiqueta.place(x=20, y=20)
    mi_caja = Entry(font=("Arial", 18))
    mi_caja.place(x=20, y=60)

mi_aplicacion = Tk()

configurar_interfaz_usuario()

mi_aplicacion.mainloop()