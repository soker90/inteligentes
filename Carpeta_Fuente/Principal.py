#!/usr/bin/python3
from time import time
import distancia
import networkx as nx
from Estado import Estado
from EspacioEstados import EspacioEstados
from Problema import Problema
from frontera import Frontera
from nodoBusqueda import nodoBusqueda
import sys
import gpxpy
import gpxpy.gpx

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
    #G.add_nodes_from(list(tabla_nodos.keys()))

    for way in ways:
        i=0
        for n in way['data']['nd']:
            if(len(way['data']['nd'])-1>i):
                nodo1=way['data']['nd'][i]
                nodo2=way['data']['nd'][i+1]
                nodo1Dat=tabla_nodos.get(nodo1)
                nodo2Dat=tabla_nodos.get(nodo2)
                G.add_node(nodo1)
                G.node[nodo1]['lat']= nodo1Dat[0]
                G.node[nodo1]['lon']= nodo1Dat[1]
                G.add_node(nodo2)
                G.node[nodo2]['lat']= nodo2Dat[0]
                G.node[nodo2]['lon']= nodo2Dat[1]
                G.add_edge(nodo1,nodo2)
                G.edge[nodo1][nodo2]['weight']= distancia.dist(nodo1Dat[1],nodo1Dat[0],nodo2Dat[1],nodo2Dat[0])
                i=i+1
    return G

def BusquedaBasica(problema, estrategia, maxProf,grafo):
    frontera=Frontera()
    problema.tabla.clear()
    n_inicial=nodoBusqueda(0, None, problema.estadoInicial, 0,None,0,0)
    frontera.Insertar(n_inicial)
    solucion=False

    while (not(solucion) and not(frontera.EsVacia())):

        n_actual=frontera.Elimina()
        if problema.EstadoMeta(n_actual.estado):
            solucion=True
            n_solucion=n_actual
        else:
            LS=problema.espacioEstados.sucesores(grafo,n_actual.estado)
            LN=problema.CrearListaNodos(LS, n_actual, maxProf,estrategia, grafo)
            frontera.InsertarLista(LN)

    if solucion==True:

        return problema.CrearSolucion(n_solucion)
    else:
        return None


def BusquedaIncremental(problema, estrategia, maxProf, incProf,grafo):
    profActual = incProf
    solucion=None

    while((profActual<=maxProf)and(solucion==None)):
        solucion = BusquedaBasica(problema,estrategia,profActual,grafo)
        profActual = profActual + incProf

    return solucion

def crearProblema(nodoInicial,Nodos):
    estado = Estado(nodoInicial,Nodos,grafo.node[nodoInicial]['lat'],grafo.node[nodoInicial]['lon'])
    problema = Problema(espacioEstados, estado)

    return problema,estado
def nodosVisitantes():
    print("#############################")
    print("########### MENU ############")
    print("#############################")
    print("1. Complejidad pequeña")
    print("2. Complejidad mediana")
    print("3. Complejidad grande")
    print("#############################")
    print("Elige una opción")
    opcion = input()

    if opcion == str(1):
        nodoInicial = 812954564
        nodos = [803292583,812954600]
    elif opcion == str(2):
        nodoInicial = 812954564
        nodos = [803292583,814770975]
    elif opcion == str(3):
        nodoInicial = 812954564
        nodos = [836098125,812954600]

    return nodoInicial,nodos

def menu():
    print("#############################")
    print("########### MENU ############")
    print("#############################")
    print("1. Busqueda en anchura")
    print("2. Coste Uniforme")
    print("3. Busqueda en profundidad")
    print("4. Busqueda voraz")
    print("5. Busqueda A*")
    print("#############################")
    print("Elige una opción")
    opcion = input()

    print("#############################")
    print("inserte profundidad maxima")
    print("#############################")
    prof=int(input())

    print("#############################")
    print("inserte el incremento de profundidad")
    print("#############################")
    profInc=int(input())

    start_time = time()

    if opcion == str(1):
        solucion = BusquedaIncremental(problema,'anchura', prof,profInc, grafo)
    elif opcion == str(2):
        solucion = BusquedaIncremental(problema,'CosteUniforme', prof,profInc, grafo)
    elif opcion == str(3):
        solucion = BusquedaIncremental(problema,'profundidad', prof,profInc, grafo)
    elif opcion == str(4):
        solucion = BusquedaIncremental(problema,'voraz', prof,profInc, grafo)
    elif opcion == str(5):
        solucion = BusquedaIncremental(problema,'A', prof,profInc, grafo)

    elapsed_time = time() - start_time

    print("La complejidad temporal es: " + str(elapsed_time))
    print("La complejidad espacial es: " + str(problema.contador))
    return solucion

print("Introduce el nodo de origen")
nodoInicial,nodos = nodosVisitantes()


espacioEstados=EspacioEstados(-3.93,38.980,-3.92,38.999)
tabla_nodos,ways=lectura(espacioEstados)
grafo=grafo(tabla_nodos,ways)


problema,estado = crearProblema(nodoInicial,nodos)
del(tabla_nodos)
solucion = menu()



if not(solucion == None):
    solucion.reverse()

    with open("solucion.txt","w") as f:
        for sol in solucion:
            f.write(sol.__str__())
    gpx = gpxpy.gpx.GPX()
    gpx.name = "Mi gpx"
    gpx_wpt = gpxpy.gpx.GPXWaypoint(estado.lat,estado.lon,elevation="0")
    gpx.waypoints.append(gpx_wpt)
    for wpt in estado.objetivos:
        nodo = grafo.node[wpt]
        gpx_wpt = gpxpy.gpx.GPXWaypoint(nodo["lat"],nodo["lon"],elevation="0")
        gpx.waypoints.append(gpx_wpt)



    gpx_track = gpxpy.gpx.GPXTrack(name="Mi gpx",number=1)
    gpx.tracks.append(gpx_track)
    gpx_segment = gpxpy.gpx.GPXTrackSegment()
    gpx_track.segments.append(gpx_segment)


    for sol in solucion:
        gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(sol.estado.lat, sol.estado.lon, elevation=0))


    with open("solucion.gpx","w") as f:
        f.write(gpx.to_xml())
    print('Created GPX')
else:
    print("no hay solucion")





