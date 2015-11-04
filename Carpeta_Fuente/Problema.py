from EspacioEstados import EspacioEstados
from nodoBusqueda import nodoBusqueda
class Problema():

    def __init__(self,espacioEstados,estadoInicial):
        self.espacioEstados = espacioEstados
        self.estadoInicial = estadoInicial
        #self.espacioEstados.definirEstados(estadoInicial, estadoObjetivo)


    def EstadoMeta(self,Estado):
        return self.espacioEstados.objetivo(Estado)

    def CrearListaNodos(self,listaSucesores, nodoAct, maxProf, estrategia):
        contador=1
        ListaNodos=[]

        for e in listaSucesores:
            '''
            id=id+1
            estado=e[1]
            costo=e[2]
            accion=e[0]
            '''
            if estrategia=='anchura':
                valor=nodoAct.profundidad+1
            elif estrategia=='CosteUniforme':
                valor=nodoAct.costo+e[2]
            elif estrategia=='profundidad':
                valor=float(1/(nodoAct.profundidad+1))

            if(nodoAct.profundidad < maxProf):
                ListaNodos.append(nodoBusqueda(nodoAct.id+contador,nodoAct,e[1], (e[2]+nodoAct.costo), e[0], nodoAct.profundidad+1, valor))
            contador+=1

        return ListaNodos

    def CrearSolucion(self,nodoAct):

        NodosSolucion = []
        NodosSolucion.append(nodoAct)
        nodo=nodoAct.padre
        while( not(nodo.padre==None)):
            NodosSolucion.append(nodo)
            nodo=nodo.padre

        return NodosSolucion

