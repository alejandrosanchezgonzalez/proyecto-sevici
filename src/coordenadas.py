import csv
import math 
import folium
from collections import namedtuple





Coordenadas = namedtuple('Coordenadas', 'latitud, longitud')
# Creación de un tipo de namedtuple para las estaciones
# type: Estacion(str, int, int, int, Coordenadas(float, float))
Estacion = namedtuple('Estacion', 'nombre, bornetas, bornetas_vacias, bicis_disponibles, ubicacion')