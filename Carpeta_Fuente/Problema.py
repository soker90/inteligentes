
from nodoBusqueda import nodoBusqueda
import distancia

class Problema():

    def __init__(self,espacioEstados,estadoInicial):
        self.espacioEstados = espacioEstados
        self.estadoInicial = estadoInicial
        self.contador=1
        self.lista_valores={}
        self.tabla = {}




    def EstadoMeta(self,Estado):

        return self.espacioEstados.objetivo(Estado)

    def CrearListaNodos(self,listaSucesores, nodoAct, maxProf, estrategia, tabla_nodos):

        ListaNodos=[]
        podar=False
        for e in listaSucesores:
            if estrategia=='anchura':
                valor=nodoAct.profundidad+1
                podar=self.poda(nodoAct)
            elif estrategia=='CosteUniforme':
                valor=nodoAct.costo+e[2]
                podar=self.poda(nodoAct)
            elif estrategia=='profundidad':
                valor=(1/(nodoAct.profundidad+1))
                podar=self.poda(nodoAct)
            elif estrategia=='voraz':
                valor=self.Heuristica(nodoAct.estado, tabla_nodos)
                podar=self.poda(nodoAct)
            elif estrategia=='A':
                valor=(nodoAct.costo+e[2]) + self.Heuristica(nodoAct.estado, tabla_nodos)
                podar=self.poda(nodoAct)
            if(nodoAct.profundidad < maxProf and podar==False):
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



    def poda(self, nodo):
        if not(nodo.estado.__str__() in self.tabla.keys()):
            self.tabla[nodo.estado.__str__()] = nodo.valor
            return False
        elif (self.tabla.get(nodo.estado.__str__()) <= nodo.valor):
            return True
        else:
            self.tabla[nodo.estado.__str__()] = nodo.valor
            return False



    def Heuristica(self,estado,tabla_nodos):
        origen = tabla_nodos.get(estado.localizacion)
        costes=[]
        for objetivo in estado.objetivos:
            destino = tabla_nodos.get(objetivo)
            costes.append(distancia.dist(origen[1],origen[0],destino[1],destino[0]))
        return max(costes)

'''
    def poda(self,nodo):
        print(nodo.estado.localizacion)
        if not(nodo.estado in self.lista_valores.keys()):
            self.lista_valores[nodo.estado.__str__()]=nodo.valor
            print(self.lista_valores)
            print("no esta en la lista y no poda")
            return False

        else:
            if(nodo.valor<self.lista_valores[nodo.estado.__str__()]):
                self.lista_valores[nodo.estado.__str__()]=nodo.valor
                print("actualiza y no poda")
                return False
            else:
                print("Si poda")
                return True
'''

