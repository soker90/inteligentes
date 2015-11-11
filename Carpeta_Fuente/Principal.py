#!/usr/bin/python3

import distancia
import networkx as nx
from Estado import Estado
from EspacioEstados import EspacioEstados
from Problema import Problema
from frontera import Frontera
from nodoBusqueda import nodoBusqueda

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

def BusquedaBasica(problema, estrategia, maxProf,grafo,tabla_nodos):
    frontera=Frontera()
    n_inicial=nodoBusqueda(0, None, problema.estadoInicial, 0,None,0,0)
    frontera.Insertar(n_inicial)
    solucion=False

    while (not(solucion) and not(frontera.EsVacia())):

        n_actual=frontera.Elimina()
        if problema.EstadoMeta(n_actual.estado):
            solucion=True
        else:

            LS=problema.espacioEstados.sucesores(grafo,n_actual.estado)
            LN=problema.CrearListaNodos(LS, n_actual, maxProf,estrategia,tabla_nodos)
            frontera.InsertarLista(LN)




    if solucion==True:
        return problema.CrearSolucion(n_actual)
    else:
        return None


def BusquedaIncremental(problema, estrategia, maxProf, incProf,grafo,tabla_nodos):
    profActual = incProf
    solucion=None
    while( not(solucion) and profActual<=maxProf):
        solucion = BusquedaBasica(problema,estrategia,profActual,grafo,tabla_nodos)
        profActual = profActual + incProf
    return solucion





problema = Problema(EspacioEstados(-3.9326000,38.9836000,-3.9217000,38.98839000),Estado(812954564,[803292583,812954600]))

tabla_nodos,ways=lectura(problema.espacioEstados)
grafo=grafo(tabla_nodos,ways)


solucion = BusquedaIncremental(problema,'voraz', 50,50, grafo,tabla_nodos)

solucion.reverse()



with open("solucion.txt","w") as f:
    for sol in solucion:
        f.write(sol.__str__())




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
