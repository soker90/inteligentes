
from nodoBusqueda import nodoBusqueda
import distancia

class Problema():

    def __init__(self,espacioEstados,estadoInicial):
        self.espacioEstados = espacioEstados
        self.estadoInicial = estadoInicial
        self.contador=1


    def EstadoMeta(self,Estado):

        return self.espacioEstados.objetivo(Estado)

    def CrearListaNodos(self,listaSucesores, nodoAct, maxProf, estrategia,tabla_nodos):

        ListaNodos=[]

        for e in listaSucesores:

            if estrategia=='anchura':
                valor=nodoAct.profundidad+1
            elif estrategia=='CosteUniforme':
                valor=nodoAct.costo+e[2]
            elif estrategia=='profundidad':
                valor=(1/(nodoAct.profundidad+1))
            elif estrategia=='voraz':
                valor=self.Heuristica(nodoAct.estado,tabla_nodos)
            elif estrategia=='A':
                valor=(nodoAct.costo+e[2]) + self.Heuristica(nodoAct.estado,tabla_nodos)


            if(nodoAct.profundidad < maxProf):
                ListaNodos.append(nodoBusqueda(self.contador, nodoAct,e[1], (e[2]+nodoAct.costo), e[0], nodoAct.profundidad+1, valor))
            self.contador = self.contador + 1

        return ListaNodos

    def CrearSolucion(self,nodoAct):

        NodosSolucion = []
        NodosSolucion.append(nodoAct)
        nodo=nodoAct.padre
        while( not(nodo.padre==None)):
            NodosSolucion.append(nodo)
            nodo=nodo.padre
        NodosSolucion.append(nodo)

        return NodosSolucion

    def Heuristica(self,estado,tabla_nodos):
        origen = tabla_nodos.get(estado.localizacion)
        heuristica=0
        for objetivo in estado.objetivos:
            destino = tabla_nodos.get(objetivo)
            costo = distancia.dist(origen[1],origen[0],destino[1],destino[0])
            if(costo>heuristica):
                heuristica=costo

        print(heuristica)
        return heuristica
