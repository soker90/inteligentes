#!/usr/bin/python3

import distancia
import networkx as nx
from lxml import etree

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
                G.edge[nodo1][nodo2]['weight']= distancia.dist(nodo1Dat[1],nodo1Dat[0],nodo2Dat[1],nodo2Dat[0])
                i=i+1
    return G




tabla_nodos,ways=lectura()
grafo=grafo(tabla_nodos,ways)
print("nodos: " + str(grafo.nodes()))
print("Inserte id de nodo")
cadena = input()
adyacentes=grafo.neighbors(cadena)
print(str(adyacentes))
cadena2=input()
print(grafo.edge[cadena][cadena2]['weight'])

