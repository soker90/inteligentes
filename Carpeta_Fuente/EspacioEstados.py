import Estado
import Principal
import networkx as nx

class EspacioEstados():
    def __init__(self, grafo):
        self.espacioEstados = grafo
        self.acciones=[["N",1,0],["NE",1,1],["E",0,1],["SE",-1,1],["S",-1,0],["SO",-1,-1],["O",0,-1],["NO",1,-1]]

        self.estadoActual= None
        self.estadoFin = None


    def definirEstados(self,actual, fin):
        self.estadoActual = actual
        self.estadoFin = fin


    def valido(self, estado):
        if self.estadoActual.localizacion in grafo.neighbors(estado.localizacion):
            return True
        else:
            return False

    def objetivo(self,estado):
        if estado == self.estadoFin:
            return True
        else:
            return False

    def sucesores(self,estado):
        sucesores=[]



        vecinos = self.espacioEstados.neighbors(estado.localizacion)

        for key in vecinos:
            N=0
            S=0
            E=0
            O=0
            nodo1=Principal.tabla_nodos.get(estado.localizacion)
            nodo2=Principal.tabla_nodos.get(key)
            cuenta = [int(nodo1[0])-int(nodo2[0]),int(nodo1[1])-int(nodo2[1])]
            if cuenta[0] > 0:
                #latitud
                O=1
            elif cuenta[0] < 0:
                E=1

            if cuenta [1] > 0:
                S = 1
            elif cuenta[1] < 0:
                N = 1


