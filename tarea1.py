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
    return info_nodos,ways


def grafo(tabla_nodos,ways):
    G=nx.Graph()
    G.add_nodes_from(tabla_nodos)
    #










tabla_nodos,ways=lectura()
grafo(tabla_nodos,ways)
