"""
Modificar cada elemento de la lista, agregando un número al principio.
Usando for
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

iterador = 0
for cancion in canciones:
    #print(f"{iterador}. {cancion}")
    canciones[iterador] = f"{iterador+1}. {canciones[iterador]}"
    iterador = iterador + 1
    
print(canciones)