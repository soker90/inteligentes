
from nodoBusqueda import nodoBusqueda
class Problema():

    def __init__(self,espacioEstados,estadoInicial):
        self.espacioEstados = espacioEstados
        self.estadoInicial = estadoInicial
        self.contador=1
        #self.espacioEstados.definirEstados(estadoInicial, estadoObjetivo)


    def EstadoMeta(self,Estado):

        return self.espacioEstados.objetivo(Estado)

    def CrearListaNodos(self,listaSucesores, nodoAct, maxProf, estrategia):

        ListaNodos=[]

        for e in listaSucesores:

            if estrategia=='anchura':
                valor=nodoAct.profundidad+1
            elif estrategia=='CosteUniforme':
                valor=nodoAct.costo+e[2]
            elif estrategia=='profundidad':
                valor=(1/(nodoAct.profundidad+1))

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

