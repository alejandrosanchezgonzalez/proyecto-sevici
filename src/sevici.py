import csv
from math import *
import folium
from collections import namedtuple
from coordenadas import *


def lee_estaciones(fichero):
    estaciones = []
    with open(fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for nombre,bornetas,bornetas_vacias,bicis_disponibles,latitud,longitud in lector:
            bornetas = int(bornetas)
            bornetas_vacias = int(bornetas_vacias)
            bicis_disponibles = int(bicis_disponibles)
            latitud = float(latitud)
            longitud = float(longitud)
            ubicacion = Coordenadas(latitud, longitud)
            estacion = Estacion(nombre, bornetas, bornetas_vacias, bicis_disponibles, ubicacion)
            estaciones.append(estacion)
    return estaciones

def estaciones_bicis_libres(estaciones, k=5):
    resultado = []
    for e in estaciones:
        if e.bornetas_vacias >= k:
            resultado.append((e.bornetas_vacias, e.nombre.split('_'), e.ubicacion))
    resultado.sort(reverse=True)
    return resultado

def calcula_distancia(coordenadas1, coordenadas2):
    return sqrt((coordenadas2.latitud - coordenadas1.latitud)**2 +
                (coordenadas2.longitud - coordenadas1.longitud)**2)

def estaciones_cercanas(estaciones, coordenadas, k=5):
    cercanas = []
    for e in estaciones:
        if e.bornetas_vacias > 0:
            dist = calcula_distancia(coordenadas, e.ubicacion)
            cercanas.append((dist, e.nombre, e.bornetas_vacias))
    cercanas.sort(key=lambda x: x[0])
    return cercanas[:k]
