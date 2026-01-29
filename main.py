# Este es el archivo principal de nuestro proyecto
# Objetivo: Crear un bot de recomendaciones

from random import *

print("¿Qué quieres que te recomiende hoy?")
ans = int(input("1. Películas \n 2. Series \n 3. Videojuegos \n"))

# Tarea 1 - Leo: Crear lista de películas
lista_peliculas = list()
lista_peliculas.append("Interstellar")
lista_peliculas.append("Frankenstein")
lista_peliculas.append("Sonic")
lista_peliculas.append("Lilo y Stitch")

# Tarea 2 - Mati: Crear lista de series
lista_series = list()
lista_series.append("The Last of Us")
lista_series.append("Andor")
lista_series.append("The Mandalorian")

# Tarea 3 - Naiyah: Crear lista de videojuegos
lista_videojuegos = list()
lista_videojuegos.append("Granny")
lista_videojuegos.append("Yandere Simulator")

if len(lista_series) != 0:
    i= randint(0, len(lista_series)-1)
    opcion_series = lista_series[i]
else:
    opcion_series = "Vacío"
if len(lista_peliculas) != 0:
    j = randint(0, len(lista_peliculas)-1)
    opcion_pelis = lista_peliculas[j] 
else:
    opcion_pelis = "Vacío"
if len(lista_videojuegos) != 0:
    k = randint(0, len(lista_videojuegos)-1)
    opcion_videos = lista_videojuegos[k]
else:
    opcion_videos = "Vacío"

if ans == 1:
    print("Te recomiendo la película:", opcion_pelis)
elif ans == 2:
    print("Te recomiendo la serie:", opcion_series)
elif ans == 3:
    print("Te recomiendo el videojuego:", opcion_videos)
else:
    print("Ingresa una opción válida.")

# Haré más modificaciones aquí, veamos que pasa si cometo un error
'''
a = input("¿quieres otra recomendación? Sí/No: ")
if a == "sí":
    pass
else:
    print("error")
'''