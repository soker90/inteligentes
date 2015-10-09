#!/usr/bin/python3

import sys
import lxml
import math
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
                #print((way.findall("nd")[i]).attrib["ref"],":",(way.findall("nd")[i+1]).attrib["ref"])
                G.add_edge((way.findall("nd")[i]).attrib["ref"],(way.findall("nd")[i+1]).attrib["ref"])
                i=i+1














tabla_nodos,ways=lectura()
grafo(tabla_nodos,ways)
