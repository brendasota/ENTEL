import math
import numpy
import pandas as pd
from geopy import distance


def dist_Haversine(lat1,lat2,long1,long2):
    rad=numpy.pi/180
    dlat=lat2-lat1
    dlon=long2-long1
    R=6372795.4775
    a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
    distancia=2*R*math.asin(math.sqrt(a))
    return distancia

def dist_geo(lat1,lat2,long1,long2):
    distance=numpy.sqrt((lat1-lat2)**2+(long1-long2)**2)*100000
    return distance

def distancia1(lat1,lat2,long1,long2):
    coord_origen=(lat1,long1)
    coord_destino=(lat2,long2)
    dist = distance.distance(coord_origen,coord_destino)
    return dist


with open("train.csv",newline="") as Archivo:
    df = pd.read_csv(Archivo)
    for i in range(2):
        print(round(dist_Haversine(df.LATITUD_ORIGEN[i],df.LATITUD_DESTINO[i],df.LONGITUD_ORIGEN[i],df.LONGITUD_DESTINO[i]),1),end=" ")
        print(round(dist_geo(df.LATITUD_ORIGEN[i],df.LATITUD_DESTINO[i],df.LONGITUD_ORIGEN[i],df.LONGITUD_DESTINO[i]),1),end=" ")
        print(distancia1(df.LATITUD_ORIGEN[i],df.LATITUD_DESTINO[i],df.LONGITUD_ORIGEN[i],df.LONGITUD_DESTINO[i]),end=" ")
        print(df.DISTANCIA[i])
    
Prueba 26

