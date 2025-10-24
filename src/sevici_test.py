from sevici import *

def test_lee_estaciones(estaciones):
    print("Las tres primeras son :")
    for estacion in estaciones[:3]:
        print(estacion)

def test_estaciones_bicis_libres(estaciones):
    for k in [5, 10, 1]:
        resultado = estaciones_bicis_libres(estaciones, k)
        print(f"\nHay {len(resultado)} estaciones con {k} o más bicis libres y las 5 primeras son:")
        for r in resultado[:5]:
            print(r)



def test_estaciones_cercanas(estaciones):
    punto = Coordenadas(37.357659, -5.9863)
    resultado = estaciones_cercanas(estaciones, punto, k=5)
    print(f"Las 5 estaciones más cercanas al punto {punto.latitud}, {punto.longitud} son:")
    for r in resultado:
        print(r)

# Ejecutar
if __name__ == "__main__":
    estaciones = lee_estaciones("data\estaciones.csv")
    test_estaciones_cercanas(estaciones)
    test_estaciones_bicis_libres(estaciones)
    test_lee_estaciones(estaciones)