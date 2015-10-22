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
        if self.estadoActual.localizacion in self.espacioEstados.neighbors(estado.localizacion):
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
            tablas = Principal()
            nodo1=tablas.tabla_nodos.get(estado.localizacion)
            nodo2=tablas.tabla_nodos.get(key)
            cuenta = [int(nodo1[0])-int(nodo2[0]),int(nodo1[1])-int(nodo2[1])]
            accion = None
            if cuenta[0] > 0:
                #latitud
                O=1
            elif cuenta[0] < 0:
                E=1

            if cuenta [1] > 0:
                #longitud
                S = 1
            elif cuenta[1] < 0:
                N = 1

            if O==1:
                if N==1:
                    accion=self.acciones[7]
                if S==1:
                    accion=self.acciones[5]
                else:
                    accion=self.acciones[6]
            elif E==1:
                if N==1:
                    accion=self.acciones[1]
                if S==1:
                    accion=self.acciones[3]
                else:
                    accion=self.acciones[2]
            elif N==1:
                accion=self.acciones[0]
            else:
                accion=self.acciones[4]


            costo=self.espacioEstados.edge[estado.localizacion][key]['weight']
            sucesores.append((accion,Estado(key,self.espacioEstados.neighbors(key)),costo))
        return sucesores
