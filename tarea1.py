#!/usr/bin/python3

import sys
import lxml
import math
import distancia
import networkx as nx


from lxml import etree

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
	x1=merc_x(float(p1lon))
	x2=merc_x(float(p2lon))
	y1=merc_y(float(p1lat))
	y2=merc_y(float(p2lat))
	return math.sqrt((x1-x2)**2+(y1-y2)**2)


def lectura():
    doc = etree.parse('ciudadreal.osm')
    raiz=doc.getroot()
    ways=raiz.findall("way")
    tipos = ["residential","trunk","pedestrian"]
    ways_sel = [] #filtro de caminos
    id_nodos = []
    for way in ways:
        if(not way.find('tag') is None):
            if(way.find('tag').attrib["k"] == "highway"  and way.find('tag').attrib["v"] in tipos):
                ways_sel.append(way)
                for n in way.findall("nd"):
                    id_nodos.append(n.attrib["ref"]) #Añade a la lista los nodos de las vias que cumplen los requisitos


    id_nodos = list(set(id_nodos)) #Quita los nodos duplicadosgg
    nodes = raiz.findall("node")
    info_nodos = {}

    #Crea un diccionario con el id del nodo como key y con la latitud y la longitud de valores
    for node in nodes:
        if(node.attrib["id"] in id_nodos):
            info_nodos[node.attrib["id"]] = [node.attrib["lat"],node.attrib["lon"]]

    return info_nodos,ways_sel


def grafo(tabla_nodos,ways):
    G=nx.Graph() #creamos el grafo
    G.add_nodes_from(list(tabla_nodos.keys()))

    for way in ways:
        i=0
        for n in way.findall("nd"):
            if(len(way.findall("nd"))-1>i):
                nodo1=(way.findall("nd")[i]).attrib["ref"]
                nodo2=(way.findall("nd")[i+1]).attrib["ref"]
                nodo1Dat=tabla_nodos.get(nodo1)
                nodo2Dat=tabla_nodos.get(nodo2)
                #print((way.findall("nd")[i]).attrib["ref"],":",(way.findall("nd")[i+1]).attrib["ref"])
                G.add_edge(nodo1,nodo2)
                G.edge[nodo1][nodo2]['weight']= dist(nodo1Dat[1],nodo1Dat[0],nodo2Dat[1],nodo2Dat[0])
                i=i+1















tabla_nodos,ways=lectura()
grafo(tabla_nodos,ways)
