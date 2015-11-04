#!/usr/bin/python3

import distancia
import networkx as nx
from Estado import Estado
from EspacioEstados import EspacioEstados
from Problema import Problema
import osmapi

def lectura(espacio):
    doc=osmapi.OsmApi().Map(espacio.lonMin,espacio.latMin,espacio.lonMax,espacio.latMax)
    tipos = ["residential","trunk","pedestrian"]
    ways=[]
    ways_sel = []
    id_nodos = []
    nodos = []
    for i in doc:
        if(i['type']=="way"):
            ways.append(i)
        elif(i['type']=='node'):
            nodos.append(i)


    for way in ways:
        if('highway' in way['data']['tag']):
            if(way['data']['tag']['highway'] in tipos):
                ways_sel.append(way)
                for n in way['data']['nd']:
                    id_nodos.append(n)

    id_nodos = list(set(id_nodos))
    info_nodos = {}

    for node in nodos:
        if(node['data']['id'] in id_nodos ):
            info_nodos[node['data']['id']] = [node['data']['lat'],node['data']['lon']]


    return info_nodos,ways_sel

    '''
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
    '''

def grafo(tabla_nodos,ways):
    G=nx.Graph() #creamos el grafo
    G.add_nodes_from(list(tabla_nodos.keys()))

    for way in ways:
        i=0
        for n in way['data']['nd']:
            if(len(way['data']['nd'])-1>i):
                nodo1=way['data']['nd'][i]
                nodo2=way['data']['nd'][i+1]
                nodo1Dat=tabla_nodos.get(nodo1)
                nodo2Dat=tabla_nodos.get(nodo2)
                #print((way.findall("nd")[i]).attrib["ref"],":",(way.findall("nd")[i+1]).attrib["ref"])
                G.add_edge(nodo1,nodo2)
                G.edge[nodo1][nodo2]['weight']= distancia.dist(nodo1Dat[1],nodo1Dat[0],nodo2Dat[1],nodo2Dat[0])
                i=i+1
    return G


def













problema = Problema(EspacioEstados(-3.93201,38.98396,-3.92111,38.98875),Estado(803292594,[814770929,2963385997,522198144]))

tabla_nodos,ways=lectura(problema.espacioEstados)
grafo=grafo(tabla_nodos,ways)
'''
print("nodos: " + str(grafo.nodes()))
print("Inserte id de nodo")
cadena = input()
adyacentes=grafo.neighbors(int(cadena))
print(str(adyacentes))
cadena2=input()
print(grafo.edge[cadena][cadena2]['weight'])

print("Sucesores de: " + str(problema.estadoInicial.localizacion) + " son: " + str(problema.estadoInicial.objetivos))
#espacio = EspacioEstados(grafo)
suc = EspacioEstados.sucesores(grafo, problema.estadoInicial)
for key in suc:
   print(key[0] + " " + key[1].__str__() + " " + str(key[2]) )
'''