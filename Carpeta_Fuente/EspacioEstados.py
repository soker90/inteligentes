from Estado import Estado
import networkx as nx

class EspacioEstados:
    def __init__(self,lonMin,latMin,lonMax,latMax):

        self.lonMin=lonMin
        self.latMin=latMin
        self.lonMax=lonMax
        self.latMax=latMax
        self.estadoFin=None
        self.estadoActual=None


    def valido(self, estado):
        if self.estadoActual.localizacion in self.neighbors(estado.localizacion):
            return True
        else:
            return False

    def objetivo(self,estado):

        if estado.objetivos.__sizeof__() == 40:
            return True
        else:
            return False

    def sucesores(self,grafo, estado):
        sucesores = []

        vecinos = grafo.neighbors(estado.localizacion)

        for key in vecinos:
            obj = []
            accion = str(estado.localizacion) + " -> " + str(key)
            costo=grafo.edge[estado.localizacion][key]['weight']
            lat=grafo.node[key]['lat']
            lon=grafo.node[key]['lon']

            for key2 in estado.objetivos:
                if not(key2 == key):
                    obj.append(key2)


            sucesores.append([accion, Estado(key, obj, lat, lon), costo])

        return sucesores



