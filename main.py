# Este es el archivo principal de nuestro proyecto
# Objetivo: Crear un bot de recomendaciones

print("¿Qué quieres que te recomiende hoy?")
ans = int(input("1. Películas \n 2. Series \n 3. Videojuegos \n"))

# Andrea: crear lista de pan dulce
lista_pan = list()
lista_pan.append("oreja")
lista_pan.append("cochinito")
lista_pan.append("ojo de buey")
lista_pan.append("dona")
lista_pan.append("concha")

# Andrea: crear lista de series
lista_series = ["Warrior Nun", "Andor", "Kenobi"]

# Tarea 1 - Jorge: Crear lista de películas
lista_peliculas = list()

# Tarea 2 - Pilar: Crear lista de libros
lista_series = list()

# Tarea 3 - Emiliano: Crear lista de videojuegos
lista_videojuegos = list()

for i in range(0, len(lista_series)):
    opcion_series = lista_series[i]
for i in range(0, len(lista_peliculas)):
    opcion_pelis = lista_peliculas[i]
for i in range(0, len(lista_videojuegos)):
    opcion_videos = lista_videojuegos[i]

if ans == 1:
    print("Te recomiendo la película: ")
elif ans == 2:
    print("Te recomiendo la serie: ")
elif ans == 3:
    print("Te recomiendo el videojuego: ")
else:
    print("Ingresa una opción válida.")

# Haré más modificaciones aquí, veamos que pasa si cometo un error

a = input("¿quieres otra recomendación? Sí/No")
if a == "sí":
    pass
else:
    print("error")
