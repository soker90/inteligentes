import espacioEstados

class Problema():

    def __init__(self,espacioEstados,estadoInicial, estadoObjetivo):
        self.espacioEstados = espacioEstados
        self.estadoInicial = estadoInicial
        self.espacioEstados.definirEstados(estadoInicial, estadoObjetivo)


    def EstadoMeta(self,Estado):
        return self.espacioEstados.objetivo(Estado)
