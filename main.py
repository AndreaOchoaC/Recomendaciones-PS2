# Este es el archivo principal de nuestro proyecto
# Objetivo: Crear un bot de recomendaciones

print("¿Qué quieres que te recomiende hoy?")
ans = int(input("1. Películas \n 2. Series \n 3. Videojuegos \n"))

# Tarea 1 - Leo: Crear lista de películas
lista_peliculas = list()

# Tarea 2 - Mati: Crear lista de series
lista_series = list()
lista_series.append("The Last of Us")
lista_series.append("Andor")
lista_series.append("The Mandalorian")

# Tarea 3 - Naiyah: Crear lista de videojuegos
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
