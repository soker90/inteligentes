#!/usr/bin/python3

import sys
import lxml
import math

from lxml import etree
def lectura():
    doc = etree.parse('ciudadreal.osm')
    raiz=doc.getroot()
    ways=raiz.findall("way")
    tipos = ["residential","trunk","pedestrian"]
    id_nodos = []
    for way in ways:
        if(not way.find('tag') is None):
            if(way.find('tag').attrib["k"] == "highway"  and way.find('tag').attrib["v"] in tipos):
                for n in way.findall("nd"):
                    id_nodos.append(n.attrib["ref"]) #Añade a la lista los nodos de las vias que cumplen los requisitos


    id_nodos = list(set(id_nodos)) #Quita los nodos duplicadosgg
    nodes = raiz.findall("node")
    info_nodos = {}

    #Crea un diccionario con el id del nodo como key y con la latitud y la longitud de valores
    for node in nodes:
        if(node.attrib["id"] in id_nodos):
            info_nodos[node.attrib["id"]] = [node.attrib["lat"],node.attrib["lon"]]
    print(info_nodos)
    return info_nodos


def grafo(nodos):


    def calcular_distancia(punto1,punto2):

        def merc_x(lon):
            r_major=6378137.000
            return r_major*math.radians(lon)

        def merc_y(lat):
            if lat>89.5:lat=89.5
            if lat<-89.5:lat=-89.5
            r_major=6378137.000
            r_minor=6356752.3142
            temp=r_minor/r_major
            eccent=math.sqrt(1-temp**2)
            phi=math.radians(lat)
            sinphi=math.sin(phi)
            con=eccent*sinphi
            com=eccent/2
            con=((1.0-con)/(1.0+con))**com
            ts=math.tan((math.pi/2-phi)/2)/con
            y=0-r_major*math.log(ts)
            return y

#Distancia entre dos punto geograficos.
#Se obtiene sus proyecciones Mercator
#y la distancia euclidea entre ellas
        def dist(p1lon,p1lat,p2lon,p2lat):
	        x1=merc_x(p1lon)
	        x2=merc_x(p2lon)
	        y1=merc_y(p1lat)
	        y2=merc_y(p2lat)
	        return sqrt((x1-x2)**2+(y1-y2)**2)






tabla_nodos=lectura()
grafo(tabla_nodos)
