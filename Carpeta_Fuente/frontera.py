import queue

class Frontera:
    def __init__(self):
        self.lista = queue.PriorityQueue()
    def Insertar(self,nodo):
        self.lista._put([nodo.valor, nodo.id, nodo])

    def InsertarLista(self, LN):
        for nodo in LN:
            self.Insertar(nodo)

    def EsVacia(self):
        if(self.lista.empty()):
            return True
        else:
            return False

    def Elimina(self):
        if(not(self.EsVacia())):
            return self.lista._get()[2]

