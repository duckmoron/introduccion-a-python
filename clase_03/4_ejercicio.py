"""
Siguiendo la lista dada, preguntar al usuario que canción desea agregar.
Luego, agregar la canción a la lista y mostrar la lista actualizada.
"""

canciones = [
    "La Bicicleta - Carlos Vives",
    "Despacito - Luis Fonsi ft. Daddy Yankee",
    "Beso en la Frente - Paulo Londra",
    "El Amante - Bad Bunny",
    "Mi Gente - J Balvin ft. Willy William",
    "Señorita - Shawn Mendes & Camila Cabello",
    "La Cumparsita - Carlos Gardel",
    "La Bamba - Los Lobos",
    "Bailando - Enrique Iglesias ft. Descemer Bueno & Gente de Zona",
    "Criminal - Luis Fonsi ft. Demi Lovato & Erika Ender",
]

nombre_cancion = input("Ingresa una canción: ")
nombre_autor = input("Ingresa el autor: ")

cancion = nombre_cancion + " - " + nombre_autor
canciones.append(cancion)
print(canciones)