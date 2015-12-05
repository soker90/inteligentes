
from nodoBusqueda import nodoBusqueda
import distancia

class Problema():

    def __init__(self,espacioEstados,estadoInicial):
        self.espacioEstados = espacioEstados
        self.estadoInicial = estadoInicial
        self.contador=1
        self.tabla = {}




    def EstadoMeta(self,Estado):
        return self.espacioEstados.objetivo(Estado)

    def CrearListaNodos(self,listaSucesores, nodoAct, maxProf, estrategia, grafo):

        ListaNodos=[]
        podar=False
        valor=0
        for e in listaSucesores:
            if estrategia=='anchura':
                valor=nodoAct.profundidad+1
                podar=self.poda(e[1], valor)
            elif estrategia=='CosteUniforme':
                valor=nodoAct.costo+e[2]
                podar=self.poda(e[1], valor)
            elif estrategia=='profundidad':
                valor=(1/(nodoAct.profundidad+1))
            elif estrategia=='voraz':
                valor=self.Heuristica(e[1], grafo)
                podar=self.poda(e[1], valor)
            elif estrategia=='A':
                valor=nodoAct.costo+ e[2] + self.Heuristica(e[1], grafo)
                podar=self.poda(e[1], valor)

            if((nodoAct.profundidad < maxProf) and (podar==False)):

                ListaNodos.append(nodoBusqueda(self.contador, nodoAct, e[1], (e[2]+nodoAct.costo), e[0], nodoAct.profundidad+1, valor))
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



    def poda(self,e, valor):
        if not(e.__str__() in self.tabla.keys()):
            self.tabla[e.__str__()] = valor
            return False

        elif self.tabla.get(e.__str__()) <= valor:
            return True
        else:
            self.tabla[e.__str__()] = valor
            return False



    def Heuristica(self,estado, grafo):
        costes=[]
        for objetivo in estado.objetivos:
            costes.append(distancia.dist(estado.lon,estado.lat,grafo.node[objetivo]['lon'],grafo.node[objetivo]['lat']))
        if not(costes.__sizeof__()==40):

            return max(costes)
        else:
            return 0



