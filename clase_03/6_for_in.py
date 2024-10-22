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

indice = 1
for cancion in canciones:
    print(f"{indice}. {cancion}")
    indice = indice + 1

print()

for cancion in canciones:
    tema, artista = cancion.split(" - ")
    print(f"Tema: {tema}")
    print(f"Artista: {artista}")
    print("---")